#!/usr/bin/python3
"""A script that generates a .tgz archive from the contents of
    web_static folder using do_pack func"""

from time import strftime
from datetime import date
from fabric.api import local


def do_pack():
    """ A script that generates a .tgz archive from the contents of
    web_static folder using do_pack func"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
