# 0x13. Firewall

## Overview:

This project focuses on configuring and managing firewall settings using `ufw` (Uncomplicated Firewall). Specifically, it involves setting up rules to block incoming traffic while allowing specific TCP ports, and configuring port forwarding to redirect traffic from one port to another.

## Files:

| File Name                   | Description                                                                      |
|-----------------------------|----------------------------------------------------------------------------------|
| 0-block_all_incoming_traffic_but | Configures `ufw` on a server to block all incoming traffic, except for TCP ports 22 (SSH), 443 (HTTPS), and 80 (HTTP) |
| 100-port_forwarding         | Copy of the `ufw` configuration file modified (/etc/ufw/before.rules) to enable port forwarding on `web-01`, redirecting TCP traffic from port 8080 to port 80 |
