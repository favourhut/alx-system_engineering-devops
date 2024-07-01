# Setting up my client config file
# Connecting through puppet

include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare file identy':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
