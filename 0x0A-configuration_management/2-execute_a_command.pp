# Create a manifest to kill the process named "killmenow"
exec { 'kill_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
}

# Notify the execution of the 'kill_process' exec resource
notify { 'kill_process_notification':
  require => Exec['kill_process'],
}

