#!/usr/bin/python3
""" this is the code solution for task two """
import os
import os.path
from fabric.api import put, run, env
env.hosts = ['34.232.69.6', '52.87.233.16']

def do_deploy(archive_path):
  """Distributes an archive to the web servers."""

  """ Check if the archive file exists. """
  if not os.path.isfile(archive_path):
    return False

  """ Get the archive filename without extension. """
  archive_filename = archive_path.split("/")[-1].split(".")[0]

  """ Upload the archive to the /tmp/ directory of the web servers. """
  put(archive_path, "/tmp/")

  """ Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web servers. """
  run('mkdir -p /data/web_static/releases/{}'.format(archive_filename))
  run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_filename, archive_filename))

  """ Delete the archive from the web servers. """
  run('rm /tmp/{}'.format(archive_filename))

  """ Delete the symbolic link /data/web_static/current from the web servers. """
  run('rm -f /data/web_static/current')

  """ Create a new the symbolic link /data/web_static/current on the web servers, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>). """
  run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_filename))

  """ Return True if all operations have been done correctly, otherwise return False. """
  return True

