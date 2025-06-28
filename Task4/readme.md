# 🔐 Basic Firewall Management - Cyber Security Internship Mini Guide

This repository demonstrates foundational firewall management skills for both Windows and Linux systems. It serves as a quick lab/tutorial with commands and explanations.

## 🔧 Tasks Overview

1. **Open firewall configuration**:
   - Windows: `Control Panel > System and Security > Windows Defender Firewall`
   - Linux (UFW): `sudo ufw status`

2. **List current rules**:
   - Windows: `netsh advfirewall firewall show rule name=all`
   - Linux: `sudo ufw status numbered`

3. **Block a specific port (e.g., Telnet on port 23)**:
   ```bash
   sudo ufw deny 23
