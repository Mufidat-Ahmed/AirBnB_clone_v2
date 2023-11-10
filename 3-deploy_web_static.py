#!/usr/bin/python3
""" This is the code solution for task 3. """

from fabric.api import local, run, env
from os.path import exists, isdir

env.hosts = ['34.232.69.6', '52.87.233.16']

def do_clean(number=0):
  """Deletes out-of-date archives.

  Args:
    number (int): The number of archives to keep.
  """

  # Get the list of all archives.
  archives = local("ls versions/").split("\n")

  # Delete all archives except for the most recent `number` archives.
  for archive in archives[:-number]:
    local("rm versions/{}".format(archive))

  # Run the same command on both web servers.
  run('for archive in $(ls "/data/web_static/releases/"); do if [[ "$archive" != "test" ]]; then rm /data/web_static/releases/"$archive"; fi; done')


if __name__ == "__main__":
  # Get the number of archives to keep from the command line.
  number = int(input("Enter the number of archives to keep: "))

  # Delete the out-of-date archives.
  do_clean(number)
