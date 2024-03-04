# Installs and configures Nginx web server with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
  ensure => installed,
}

exec { 'custom_header':
  environment => ["HOSTNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"${hostname}\";/" /etc/nginx/nginx.conf',
  provider    => shell,
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
