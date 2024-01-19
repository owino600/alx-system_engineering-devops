#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
<<<<<<< HEAD
  ensure   => '2.1.0',
  provider => 'pip3',
=======
	ensure   => '2.1.0',
		 provider => 'pip3',
>>>>>>> 7b9dfa7 (killmenow)
}
# Install werkzeug
package {
  'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
  require => Package['Flask']
}