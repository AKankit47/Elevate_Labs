import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [rules, setRules] = useState([]);
  const [formData, setFormData] = useState({
    source_ip: "",
    dest_port: "",
    protocol: "tcp",
    action: "DROP",
  });

  const fetchRules = async () => {
    const res = await axios.get("http://localhost:5000/rules");
    setRules(res.data);
  };

  const addRule = async () => {
    await axios.post("http://localhost:5000/rules", formData);
    fetchRules();
  };

  const deleteRule = async (id) => {
    await axios.delete(`http://localhost:5000/rules/${id}`);
    fetchRules();
  };

  useEffect(() => {
    fetchRules();
  }, []);

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Cloud Firewall Dashboard</h1>
      <div className="grid grid-cols-2 gap-4 mb-6">
        <input className="border p-2" placeholder="Source IP"
          value={formData.source_ip}
          onChange={(e) => setFormData({ ...formData, source_ip: e.target.value })}
        />
        <input className="border p-2" placeholder="Destination Port"
          value={formData.dest_port}
          onChange={(e) => setFormData({ ...formData, dest_port: e.target.value })}
        />
        <select className="border p-2"
          value={formData.protocol}
          onChange={(e) => setFormData({ ...formData, protocol: e.target.value })}
        >
          <option value="tcp">TCP</option>
          <option value="udp">UDP</option>
        </select>
        <select className="border p-2"
          value={formData.action}
          onChange={(e) => setFormData({ ...formData, action: e.target.value })}
        >
          <option value="ACCEPT">ACCEPT</option>
          <option value="DROP">DROP</option>
        </select>
        <button
          onClick={addRule}
          className="col-span-2 bg-blue-600 text-white py-2 rounded"
        >
          Add Rule
        </button>
      </div>

      <h2 className="text-xl font-semibold mb-2">Active Rules</h2>
      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2 border">ID</th>
            <th className="p-2 border">Source IP</th>
            <th className="p-2 border">Port</th>
            <th className="p-2 border">Protocol</th>
            <th className="p-2 border">Action</th>
            <th className="p-2 border">Delete</th>
          </tr>
        </thead>
        <tbody>
          {rules.map((rule) => (
            <tr key={rule[0]} className="text-center">
              <td className="p-2 border">{rule[0]}</td>
              <td className="p-2 border">{rule[1]}</td>
              <td className="p-2 border">{rule[2]}</td>
              <td className="p-2 border">{rule[3]}</td>
              <td className="p-2 border">{rule[4]}</td>
              <td className="p-2 border">
                <button
                  onClick={() => deleteRule(rule[0])}
                  className="bg-red-500 text-white px-3 py-1 rounded"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

