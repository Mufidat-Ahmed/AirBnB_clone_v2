#!/usr/bin/python3
""" this is the code solution for task 3 """

from datetime import datetime
from fabric.api import put, run, env
from os.path import exists, isdir
env.hosts = ['34.232.69.6', '52.87.233.16']


def do_pack():
	"""create the archive:tgz"""
	try:
		date_mk = datetime.now().strftime("%Y%m%d%H%M%S")
		if isdir("versions") is False:
			local("mkdir versions")
		filename_mk = "versions/web_static_{}.tgz".format(date_mk)
		local("tar -cvzf {} web_static".format(filename_mk))
		return filename_mk
	except:
		return None


def do_deploy(archive_path):
	""" share to the respective servers """
	if exists(archive_path) is False:
		return False
	try:
		file_n = archive_path.split("/")[-1]
		ext_mk = file_n.split(".")[0]
		path = "/data/web_static/releases/"
		put(archive_path, '/tmp/')
		run('mkdir -p {}{}/'.format(path, ext_mk))
		run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, ext_mk))
		run('rm /tmp/{}'.format(file_n))
		run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext_mk))
		run('rm -rf {}{}/web_static'.format(path, ext_mk))
		run('rm -rf /data/web_static/current')
		run('ln -s {}{}/ /data/web_static/current'.format(path, ext_mk))
		return True
	except:
		return False


def deploy():
	""" distributes n creates em archives"""
	archive_path = do_pack()
	if archive_path is None:
		return False
	return do_deploy(archive_path)
