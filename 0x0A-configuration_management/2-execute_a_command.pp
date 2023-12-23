#the code kills the process && works together with the killmenow
exec { 'killmenow':
	command => 'sr/binpkill killmenow',
	provider => 'shell',
	returns => [0, 1],
}
