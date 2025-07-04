# 🧾 Task 8: VPN Benefits and Limitations using OpenVPN (TryHackMe)

## ✅ VPN Tool Used
- **VPN Client**: OpenVPN
- **Source**: TryHackMe (VPN config file provided with labs)
- **Platform**: Linux terminal

---

## 🧪 Steps Performed

1. Downloaded the `.ovpn` configuration file from TryHackMe dashboard.
2. Opened terminal and connected to VPN using:
   ```bash
   sudo openvpn tryhackme.ovpn
   ```
3. Verified connection established with message: `Initialization Sequence Completed`
4. Visited [https://whatismyipaddress.com](https://whatismyipaddress.com) to check IP before and after connecting.
5. Confirmed traffic was encrypted by browsing HTTPS websites.
6. Disconnected VPN and compared browsing speed and IP again using the same website and [https://fast.com](https://fast.com).

---


---

## 🔐 VPN Benefits

- **IP Address Masking**: Hides your real IP and replaces it with a virtual one from the VPN server.
- **Encrypted Traffic**: All your internet data is tunneled and encrypted using strong protocols like AES-256.
- **Access to Geo-restricted Content**: Enables access to TryHackMe labs and other location-blocked content.
- **Protection on Public Wi-Fi**: Prevents man-in-the-middle attacks and sniffing on unsecured networks.
- **Anonymity Boost**: Helps obscure browsing activity from ISPs and some websites.

---

## ⚠️ VPN Limitations

- **Reduced Internet Speed**: Due to encryption overhead and routing through distant servers.
- **Not 100% Anonymous**: VPN providers may log metadata unless they follow a strict no-logs policy.
- **Free VPN Restrictions**: Limited locations, bandwidth caps, and slower performance.
- **No Protection from Phishing or Malware**: A VPN doesn’t stop you from visiting harmful websites or downloading malicious files.
- **Complex Setup for Beginners**: Manual configuration (especially on Linux) may be confusing without guidance.

---

## 📌 Conclusion

Using OpenVPN via TryHackMe provides a secure and educational way to understand how VPNs work. It demonstrates how traffic encryption, IP masking, and tunneling can protect your online identity and access. However, users must be aware of the limitations—VPNs are a great **layer** of defense but not a full replacement for responsible browsing and endpoint protection.
