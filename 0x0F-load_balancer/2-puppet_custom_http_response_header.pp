# Installs and configures Nginx web server with Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

exec { 'configure_nginx':
  command  => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/youssefelghamour permanent;/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'custom_header':
  environment => ["HOSTNAME=${hostname}"],
  command  => 'sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
  provider => shell,
}

service { 'nginx':
  ensure    => running,
}
