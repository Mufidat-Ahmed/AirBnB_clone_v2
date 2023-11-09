#!/usr/bin/python3
""" this is the code solution for task two """

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.232.69.6', '52.87.233.16']


def do_deploy(archive_path):
    """to distribute the generated repo onthe servers"""
    if exists(archive_path) is False:
    return False
try:
filename_mk = archive_path.split("/")[-1]
ext_mk = filename_mk.split(".")[0]
path = "/data/web_static/releases/"
put(archive_path, '/tmp/')
run('mkdir -p {}{}/'.format(path, ext_mk))
run('tar -xzf /tmp/{} -C {}{}/'.format(filename_mk, path, ext_mk))
run('rm /tmp/{}'.format(filename_mk))
run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext_mk))
run('rm -rf {}{}/web_static'.format(path, ext_mk))
run('rm -rf /data/web_static/current')
run('ln -s {}{}/ /data/web_static/current'.format(path, ext_mk))
return True
