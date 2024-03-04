# Installs and configures Nginx web server with Puppet

package { 'nginx':
  ensure => installed,
}

exec { 'custom_header':
  command => 'sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"<hostname>\";/" /etc/nginx/nginx.conf',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure   => running,
  enable   => true,
  provider => systemd,
}
