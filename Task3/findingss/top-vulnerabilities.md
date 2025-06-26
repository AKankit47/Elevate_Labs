
# 🔐 Top Vulnerabilities from Localhost Scan

This document summarizes the most critical and high-severity vulnerabilities identified during the Nessus scan performed on `127.0.0.1` (localhost).

---

### 🔴 **1. Node.js Multiple Vulnerabilities (CVE-2024-21892, CVE-2024-21896, CVE-2024-22019)**
- **Plugin ID:** 190856  
- **Severity:** Critical (CVSS 9.8)  
- **Description:** Multiple vulnerabilities in Node.js may allow remote code execution, denial of service, or bypass of security features.  
- **Affected Versions:** Node.js < 20.11.1  
- **Recommendation:** Upgrade to Node.js v20.11.1 or later.

---

### 🟠 **2. Node.js DoS & HTTP Smuggling (CVE-2024-27982, CVE-2024-27983)**
- **Plugin ID:** 192945  
- **Severity:** High (CVSS 8.2)  
- **Description:** Vulnerabilities in the HTTP/2 implementation of Node.js could allow an attacker to cause a denial of service or perform HTTP request smuggling.  
- **Affected Versions:** Node.js < 20.12.1  
- **Recommendation:** Upgrade to Node.js v20.12.1 or later.

---

### 🟠 **3. Node.js Permission Model Bypass (CVE-2024-27980, CVE-2024-36137, etc.)**
- **Plugin ID:** 201969  
- **Severity:** High (CVSS 8.1)  
- **Description:** Vulnerabilities in the permission model can allow unprivileged access to restricted resources.  
- **Affected Versions:** Node.js < 20.15.1  
- **Recommendation:** Upgrade to Node.js v20.15.1 or later.

---

### 🟠 **4. Node.js Memory Leak & Privilege Escalation (CVE-2025-23083)**
- **Plugin ID:** 214404  
- **Severity:** High (CVSS 7.7)  
- **Description:** Vulnerability in Node.js may result in memory leaks or privilege escalation under certain conditions.  
- **Affected Versions:** Node.js < 20.18.2  
- **Recommendation:** Upgrade to Node.js v20.18.2 or later.
