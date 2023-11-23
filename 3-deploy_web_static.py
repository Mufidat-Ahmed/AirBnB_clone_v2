#!/usr/bin/python3
"""creates and distributes an archive to your web servers
 using the function deploy"""

from fabric.api import local
from os.path import exists
from datetime import datetime
from .2-do_deploy_web_static import do_deploy
from .1-pack_web_static import do_pack

env.hosts = ['54.152.133.243', '54.237.34.128']


def deploy():
    """
    Create and deploy an archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
