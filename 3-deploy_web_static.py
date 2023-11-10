#!/usr/bin/python3
""" solution for task 3 """

from fabric.api import run, env

def do_pack():
  """Creates an archive."""

  # Create the archive.
  run('tar -cvzf versions/web_static.tgz web_static')

  # Return the path of the created archive.
  return 'versions/web_static.tgz'

def do_deploy(archive_path):
  """Distributes an archive to the web servers."""

  """ Check if the archive file exists. """
  if not exists(archive_path):
	return False

  """ Upload the archive to the web servers."""
  run('put {} /tmp/'.format(archive_path))

  """Uncompress the archive on the web servers. """
  run('tar -xzf /tmp/web_static.tgz -C /data/web_static/releases/')

  """ Delete the archive from the web servers. """
  run('rm /tmp/web_static.tgz')

  """ Create a symbolic link to the current version of the web application on the web servers. """
  run('ln -s /data/web_static/releases/web_static /data/web_static/current')

  """ Return True if all operations have been done correctly, otherwise return False. """
  return True

def deploy():
  """Creates and distributes an archive to the web servers."""

  archive_path = do_pack()

  if archive_path is None:
	return False

  return do_deploy(archive_path)

if __name__ == "__main__":
  env.hosts = ['34.232.69.6', '52.87.233.16']

  deploy()
