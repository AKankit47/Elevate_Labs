# 🔐 Cybersecurity Internship Task: Local Network Reconnaissance

## 📌 Objective
This task involves scanning the local network to identify active hosts, open ports, and potential security risks. The goal is to understand how services communicate within a network and assess exposure to threats.

---

## 🧰 Tools Used
- **Nmap 7.95** – For network scanning  
- **Wireshark (Optional)** – For deep packet inspection  
- **System** – Linux-based system  
- **Network** – Private Wi-Fi

---

## 🧪 Steps Followed

### 1. Installed Nmap
Nmap was downloaded and installed from the official website:  
🔗 [https://nmap.org/download.html](https://nmap.org/download.html)

### 2. Identified Local IP Range
Using the `ip a` (Linux) command, the IP range was identified as:


### 3. Ran Nmap SYN Scan
```bash
nmap -sS 192.168.1.0/24

