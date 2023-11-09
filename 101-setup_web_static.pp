
# Install Nginx if not already installed
class { 'nginx' }

# Create necessary directories
file {
  ensure => directory,
  path => [ '/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/current', '/data/web_static/shared' ],
  recurse => true,
  owner => 'ubuntu',
  group => 'ubuntu',
}

# Create a fake HTML file for testing
file {
  ensure => present,
  content => "<html><body>This is a test file.</body></html>",
  path => '/data/web_static/releases/test/index.html',
  owner => 'ubuntu',
  group => 'ubuntu',
}

# Create a symbolic link to the test folder
file {
  ensure => symlink,
  source => '/data/web_static/releases/test',
  target => '/data/web_static/current',
  owner => 'ubuntu',
  group => 'ubuntu',
}

# Update Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
site {
  name => 'hbnb_static',
  ensure => present,
  port => '80',
  server_name => 'anealx.tech',
  content => {
	'location /hbnb_static' => {
	  alias => '/data/web_static/current/',
	},
  },
}
