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

service { 'nginx':
  ensure    => running,
}
