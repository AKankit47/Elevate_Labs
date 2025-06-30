# 🛡️ Cyber Security Internship – Task 5  
## 📡 Wireshark Protocol Capture & Analysis

### 🧪 Objective  
Capture live network traffic using Wireshark, identify various protocols, and summarize the findings.

---

### ✅ Task Steps

1. **Installed Wireshark**  
   - Downloaded and set up the latest version on Linux.

2. **Started Capture on Active Interface**  
   - Selected my active network interface (`wlan0`) in Wireshark.

3. **Generated Traffic**  
   - Visited `example.com`, `google.com`, and pinged `8.8.8.8`.

4. **Captured for 1 Minute**  
   - Collected enough packets for analysis.

5. **Filtered Packets by Protocol**
   - Applied filters:
     - `dns`
     - `tcp`
     - `http`

6. **Identified 3+ Protocols**
   - Observed **DNS**, **TCP**, and **HTTP**.

7. **Exported Capture File**
   - Saved as `task5_network_capture.pcap`.

8. **Analyzed Packets**
   - Summarized important observations and metadata.

---

### 📊 Protocol Summary

| Protocol | Description | Example |
|----------|-------------|---------|
| **DNS**  | Domain resolution | Query: `google.com` → Response from `8.8.8.8` |
| **TCP**  | Connection handling | TCP handshake observed with `example.com` |
| **HTTP** | Website communication | GET request to `/index.html` |

---

### 📁 Files Included
- `task5_network_capture.pcap` – Exported Wireshark packet capture file.
- `README.md` – This documentation file.

---

### 🧠 Key Learnings
- Learned how to capture and analyze real network traffic.
- Understood the role of DNS, TCP, and HTTP in day-to-day communications.
- Gained hands-on experience with Wireshark’s filtering and packet inspection tools.

---

### 🔐 Author
**0xH4ck3r_4K**  
[TryHackMe: Top 15 🇮🇳 | Top 115 🌎 | Diamond League 🥇]  
*#CyberSecurity #Wireshark #Internship #PacketAnalysis #Networking*
