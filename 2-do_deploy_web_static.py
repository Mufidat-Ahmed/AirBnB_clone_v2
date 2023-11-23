#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
import os
import os.path
from fabric.api import put
from fabric.api import run
from fabric.api import env
env.hosts = ['54.152.133.243', '54.237.34.128']

def do_deploy(archive_path):
    """
    Deploy archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split('/')[-1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(archive_name, archive_name))
        run("rm /tmp/{}.tgz".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(archive_name, archive_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_name))
        return True
    except Exception:
        return False
