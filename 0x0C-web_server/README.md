# 0x0C. Web server

## Overview

This project, part of the SE Foundations curriculum, focuses on configuring a web server and automating tasks using Bash and Puppet. The tasks involve setting up Nginx, configuring domains, implementing redirections, and customizing error pages.

## Files:

| File Name                           | Description                                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 0-transfer_file                     | Bash script to transfer a file from the client to the server using SCP.                                               |
| 1-install_nginx_web_server          | Installs Nginx on web-01, configures it to listen on port 80, and returns "Hello World!" at root.                      |
| 2-setup_a_domain_name               | Provides a .tech domain name and configures DNS records with an A entry pointing to web-01's IP address.              |
| 3-redirection                       | Configures Nginx to redirect /redirect_me to another page with a "301 Moved Permanently" status.                       |
| 4-not_found_page_404                | Configures Nginx to have a custom 404 page containing the string "Ceci n'est pas une page."                            |
| 7-puppet_install_nginx_web_server.pp | Puppet manifest that installs and configures Nginx |
