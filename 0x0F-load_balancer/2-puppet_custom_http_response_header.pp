# Installs and configures Nginx web server with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
} ->

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx'
} ->

file_line { 'custom_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
} ->

exec {'start nginx':
  command => '/usr/sbin/service nginx start',
}
