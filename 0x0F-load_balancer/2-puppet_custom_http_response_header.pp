# Installs and configures Nginx web server with Puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update'
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx'
}

exec { 'custom_header':
  provider    => shell,
  environment => ["HOSTNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf'
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
