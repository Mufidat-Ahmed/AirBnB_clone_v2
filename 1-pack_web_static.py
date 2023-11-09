#!/usr/bin/python3
""" this is the solution for task 1 """

import os.path
from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """this is to create a tgz repo"""
    try:
    date_mk = datetime.now().strftime("%Y%m%d%H%M%S")
if isdir("versions") is False:
    local("mkdir versions")
filename_mk = "versions/web_static_{}.tgz".format(date_mk)
local("tar -cvzf {} web_static".format(filename_mk))
return filename_mk
