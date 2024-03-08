# 0x10. HTTPS SSL

## Overview

This project focuses on HTTPS SSL configuration, including DNS setup, SSL termination using HAproxy, and enforcing HTTPS traffic. Tasks involve configuring domain zones, creating certificates, and ensuring secure encrypted communication.

## Files

| File Name                 | Description |
| ------------------------- | ----------- |
| 0-world_wide_web          | Bash script for configuring domain subdomains and displaying information about them. |
| 1-haproxy_ssl_termination | HAproxy configuration for SSL termination on subdomain www with a certificate obtained using certbot. |
| 100-redirect_http_to_https | HAproxy configuration for automatically redirecting HTTP traffic to HTTPS. |
| haproxy_https_ssl_configuration_guide | Steps to configure HAProxy with HTTPS and SSL using Certbot for SSL/TLS certificate setup. |
