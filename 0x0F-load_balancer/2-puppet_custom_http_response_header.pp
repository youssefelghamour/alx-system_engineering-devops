# Installs and configures Nginx web server with Puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}

-> package {'nginx':
  ensure => 'present',
}

-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

-> service { 'nginx':
  command => '/usr/sbin/service nginx start',
}
