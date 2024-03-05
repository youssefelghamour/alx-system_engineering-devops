# 0x0F. Load balancer

## Overview

This project focuses on enhancing web server redundancy and reliability by configuring an additional server web-02 to the already configured server web-01, behind a load balancer lb-01. The tasks involve automating the setup using Bash scripts and Puppet to ensure consistency and efficiency. The load balancer distributes traffic using a round-robin algorithm, and custom HTTP headers are added in the HTTP response of both the web-01 and web-02 servers to track which web server handles requests: The name of the custom HTTP header is X-Served-By (ex: X-Served-By: 511149-web-01).

## Files

| File                                        | Description                                       |
| ------------------------------------------- | ------------------------------------------------- |
| `0-custom_http_response_header`             | Configures Nginx on the server with custom headers.               |
| `1-install_load_balancer`                   | Installs and configures HAProxy on lb-01 for load balancing.             |
| `2-puppet_custom_http_response_header.pp`   | Puppet script for automating custom HTTP header configuration.  |
| `web-01`                                    | Bash script to connect to the web-01 server  |
| `web-02`                                    | Bash script to connect to the web-02 server   |
| `lb-01`                                     | Bash script to connect to the lb-01 server    |
