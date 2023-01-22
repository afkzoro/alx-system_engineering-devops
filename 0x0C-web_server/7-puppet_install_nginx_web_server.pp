# Installs Nginx on Ubuntu


package { 'apache2.2-common':
    ensure => absent,
  }
package { 'nginx':
    ensure  => installed,
    require => Package['apache2.2-common'],
  }
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
  }

server { 'nginx':
    listen => 80,
}
