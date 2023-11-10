#!/usr/bin/python3
""" solution for task 101 """
from fabric.api import run, env

def do_clean(number=0):
  """Deletes out-of-date archives.

  Args:
    number (int): The number of archives to keep.
  """

  archives = run("ls versions/").split("\n")

  for archive in archives[:-number]:
    run("rm versions/{}".format(archive))

  run('for archive in $(ls "/data/web_static/releases/"); do if [[ "$archive" != "test" ]]; then rm /data/web_static/releases/"$archive"; fi; done')

if __name__ == "__main__":
  env.hosts = ['34.232.69.6', '52.87.233.16']

  number = int(input("Enter the number of archives to keep: "))

  do_clean(number)
