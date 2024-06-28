# kill a running process

exec { 'killmenow':
command  => 'pkill -9 killmenow',
provider => 'shell',
}
