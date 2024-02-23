# 0x0A. Configuration management

This project is a basic example of configuration management using Puppet. It includes Puppet manifests for performing simple tasks such as creating files, executing commands, and managing packages.

## Files

| Filename                                        | Description                                                                        |
| ----------------------------------------------- | ---------------------------------------------------------------------------------- |
| 0-create_a_file.pp        | Creates a file in `/tmp` with specific permissions, owner, group, and content.     |
| 1-install_a_package.pp | Installs Flask version 2.1.0 using `pip3`.                                        |
| 2-execute_a_command.pp | Executes a command using the `exec` Puppet resource to terminate a process.        |
