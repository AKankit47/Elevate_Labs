from flask import Flask, request, jsonify
import subprocess
import sqlite3
import os
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = 'firewall.db'
LOG_PATH = 'firewall.log'

# Configure logging
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s %(message)s')

# Initialize the SQLite database
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_ip TEXT,
                dest_port INTEGER,
                protocol TEXT,
                action TEXT
            )
        """)
        conn.commit()
        conn.close()

init_db()

# GET all firewall rules
@app.route('/rules', methods=['GET'])
def get_rules():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM rules")
    rules = c.fetchall()
    conn.close()
    return jsonify(rules)

# POST a new rule
@app.route('/rules', methods=['POST'])
def add_rule():
    data = request.get_json()
    source_ip = data['source_ip']
    dest_port = data['dest_port']
    protocol = data['protocol']
    action = data['action'].upper()

    rule_cmd = [
        'iptables',
        '-A', 'INPUT',
        '-s', source_ip,
        '-p', protocol,
        '--dport', str(dest_port),
        '-j', action
    ]

    try:
        subprocess.run(rule_cmd, check=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT INTO rules (source_ip, dest_port, protocol, action) VALUES (?, ?, ?, ?)",
            (source_ip, dest_port, protocol, action)
        )
        conn.commit()
        conn.close()
        logging.info(f"ADDED rule: {source_ip} -> {dest_port}/{protocol} {action}")
        return jsonify({'status': 'Rule added'}), 201
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

# DELETE a rule
@app.route('/rules/<int:rule_id>', methods=['DELETE'])
def delete_rule(rule_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT source_ip, dest_port, protocol, action FROM rules WHERE id = ?", (rule_id,))
    rule = c.fetchone()

    if not rule:
        return jsonify({'error': 'Rule not found'}), 404

    source_ip, dest_port, protocol, action = rule

    rule_cmd = [
        'iptables',
        '-D', 'INPUT',
        '-s', source_ip,
        '-p', protocol,
        '--dport', str(dest_port),
        '-j', action.upper()
    ]

    try:
        subprocess.run(rule_cmd, check=True)
        c.execute("DELETE FROM rules WHERE id = ?", (rule_id,))
        conn.commit()
        conn.close()
        logging.info(f"DELETED rule: {source_ip} -> {dest_port}/{protocol} {action.upper()}")
        return jsonify({'status': 'Rule deleted'})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
