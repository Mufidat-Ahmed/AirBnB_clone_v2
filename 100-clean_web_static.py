#!/usr/bin/python3
""" this is the code solution for task  100"""

import os
from fabric.api import *

env.hosts = ['34.232.69.6', '52.87.233.16']


def do_clean(number=0):
	""" Clean out all outdated archives """
	number = 1 if int(number) == 0 else int(number)

	arch_mk = sorted(os.listdir("versions"))
	[arch_mk.pop() for i in range(number)]
	with lcd("versions"):
		[local("rm ./{}".format(a)) for a in arch_mk]

	with cd("/data/web_static/releases"):
		arch_mk = run("ls -tr").split()
		arch_mk = [a for a in arch_mk if "web_static_" in a]
		[arch_mk.pop() for i in range(number)]
		[run("rm -rf ./{}".format(a)) for a in arch_mk]
