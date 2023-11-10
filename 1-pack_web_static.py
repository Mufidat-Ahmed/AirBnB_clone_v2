#!/usr/bin/python3
""" This is the solution for task 1. """

import os
from datetime import datetime
from fabric.api import local

def do_pack():
  """This function creates a .tgz archive from the contents of the web_static folder."""

  """ Create the versions folder if it doesn't exist. """
  if not os.path.isdir("versions"):
    local("mkdir versions")

  """ Get the current date and time. """
  now = datetime.now()

  """ Generate the archive name. """
  archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

  """ Create the archive. """
  local("tar -cvzf {} web_static".format(archive_name))

  return archive_name if os.path.isfile(archive_name) else None

""" Example usage: """

archive_path = do_pack()
if archive_path is not None:
  print("Archive created successfully:", archive_path)
else:
  print("Failed to create archive.")

