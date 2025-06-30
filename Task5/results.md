# 📊 Results – Wireshark Packet Analysis (Task 5)

## 🎯 Objective:
Analyze captured network traffic using Wireshark and identify at least three different network protocols.

---

## 🧪 Methodology:

1. Started Wireshark on the active network interface (`wlan0`).
2. Generated traffic by:
   - Visiting websites: `example.com`, `neverssl.com`
   - Pinging `8.8.8.8` from terminal
3. Captured packets for 1 minute.
4. Applied filters: `dns`, `tcp`, `http` to identify protocols.
5. Exported the session as `task5_network_capture.pcap`.

---

## 📡 Protocols Identified:

| Protocol | Function | Observation |
|----------|----------|-------------|
| **DNS**  | Domain name resolution | Queried `google.com` via `8.8.8.8` |
| **TCP**  | Reliable data transmission | Observed 3-way handshakes and data transfer |
| **HTTP** | Unencrypted web traffic | GET request to `/index.html` on `example.com` |

---

## 📍 Packet Highlights:

### 🔸 DNS
- Request: `Standard query A google.com`
- Response: `Standard query response 142.250.x.x`

### 🔸 TCP
- Handshake: SYN, SYN-ACK, ACK
- Ports involved: 80 (HTTP), 443 (HTTPS)

### 🔸 HTTP
- Method: `GET`
- Host: `example.com`
- Resource: `/index.html`
---

## 🧠 Conclusion

Successfully captured and analyzed real-world network packets using Wireshark. Identified multiple communication protocols (DNS, TCP, HTTP) and understood how they contribute to normal internet operations.

---

## 🔖 Tags
`#CyberSecurity` `#Wireshark` `#InternshipTask5` `#Networking` `#ProtocolAnalysis`
