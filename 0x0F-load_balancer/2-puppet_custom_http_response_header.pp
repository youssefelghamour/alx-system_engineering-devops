# Installs and configures Nginx web server with Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

exec { 'custom_header':
  environment => ["HOSTNAME=${hostname}"],
  command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
  provider => shell,
}

service { 'nginx':
  ensure    => running,
}
