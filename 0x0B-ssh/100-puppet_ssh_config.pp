# changes config file using puppet
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
