# Linux UFW Firewall Summary and Testing

## How Linux UFW Firewall Filters Traffic

UFW (Uncomplicated Firewall) is a user-friendly interface for managing Linux’s firewall rules, built on top of `iptables`. It filters network traffic by applying rules based on:

- Port numbers (e.g., 22 for SSH, 23 for Telnet)
- Protocols (TCP, UDP)
- Direction (inbound/outbound)

When a network packet arrives, UFW checks it against the configured rules in order. If a packet matches a **deny** rule, it is blocked. If it matches an **allow** rule, it is permitted. Any traffic not explicitly allowed is blocked by default, providing a secure baseline.

## Testing the Firewall Rules on Linux

To verify UFW’s filtering:

1. Block inbound traffic on port 23 (Telnet):

   ```bash
   sudo ufw deny 23/tcp
Attempt to connect to port 23 remotely using:

telnet <linux-ip> 23

The connection failed, confirming that port 23 was successfully blocked.

Allow SSH access on port 22:

sudo ufw allow 22/tcp

Remove the block on port 23 to restore normal access:

    List numbered rules:

sudo ufw status numbered

Delete the deny rule blocking port 23 by its rule number (for example, if rule number is 3):

sudo ufw delete 3

This testing demonstrated that UFW effectively enforces firewall policies, controlling network access and enhancing Linux system security.
