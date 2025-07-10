# 🔥 Cloud Firewall – Full Stack Project

A custom-built **cloud firewall system** that allows users to manage Linux `iptables` rules using a user-friendly **React + TailwindCSS frontend** and a **Flask + SQLite backend**. Designed to automate and secure firewall rule management in cloud or VM environments.

> ✅ Developed during the **Cybersecurity Internship at Elevate Labs**

---

## 📌 Features

- 🚀 Add, view, and delete firewall rules (ACCEPT or DROP)
- 🌐 Modern responsive UI using React + TailwindCSS
- 🧠 Backend built with Flask and SQLite
- 🔐 Uses `iptables` for real rule enforcement
- 🐳 Optional Docker support (containerize backend/frontend)
- 🧱 Easily extensible for cloud security systems

---

## 🛠 Tech Stack

| Frontend                | Backend              | Security Layer       |
|------------------------|----------------------|----------------------|
| React.js (Vite)        | Python Flask         | Linux iptables       |
| TailwindCSS            | SQLite (rule DB)     | CORS, API auth (optional) |
| Axios (API requests)   | RESTful API          | Logging & validation |

---

## 📂 Folder Structure

cloud-firewall-full/
├── backend/ # Flask API and SQLite DB
│ ├── app.py
│ ├── firewall.db
│ └── requirements.txt
├── frontend/ # React + Tailwind UI
│ ├── src/
│ ├── index.html
│ ├── tailwind.config.js
│ ├── postcss.config.js
│ └── package.json
└── README.md


---

## ⚙️ Setup Instructions

### 🖥 Backend (Flask)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo python app.py  # Run with sudo for iptables access

API runs at: http://localhost:5000

🌐 Frontend (React + Tailwind)

cd frontend
npm install
npm run dev

Frontend runs at: http://localhost:5173
-----
###
🚧 Usage Notes

1. You must run the backend with root privileges to use iptables

2. Works best on Linux VMs or cloud machines with iptables

3. All rules are stored in firewall.db for reference/logging

🧠 Future Improvements

1. 🔐 Add API key authentication

2. 📊 View rule usage and logs in the UI

3. ☁️ Deploy backend via Render/Railway

4. 💻 Deploy frontend on Netlify or Vercel


✍️ Author

Ankit Kumar
Cybersecurity Intern, Elevate Labs
GitHub: @AKankit47

📜 License

This project is for educational use only and is part of the Elevate Labs cybersecurity internship program.
