# 0x0B. SSH

## Overview
This project focuses on understanding and implementing Secure Shell (SSH) for server connections. The tasks involve creating and using SSH key pairs, configuring SSH client files, and utilizing Puppet for SSH client configuration. The project aims to enhance knowledge in server connectivity, security, and configuration.

## Files

| File Name                   | Description                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------|
| **0-use_a_private_key**     | Bash script to connect to the server using the private key `~/.ssh/school` with user `ubuntu`. |
| **1-create_ssh_key_pair**   | Bash script to create an RSA key pair named `school` with a passphrase `betty`.               |
| **2-ssh_config**            | SSH client configuration file that uses the private key `~/.ssh/school` and refuses password authentication. |
| **100-puppet_ssh_config.pp**| Puppet script to configure the SSH client to use the private key `~/.ssh/school` and refuse password authentication. |

## Learning Objectives

- Understanding the concept of servers and their typical locations.
- Knowledge of SSH and its role in secure communication.
- Creating and utilizing SSH RSA key pairs.
- Connecting to a remote host using an SSH RSA key pair.
- Configuration of SSH client files for passwordless authentication.
- Use of Puppet for SSH client configuration.
