#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name      : download retry
# Purpose   : Persistent download
#
# Authors   : Romero Dias <romero@outlook.com>
# Created   :
# Copyright : (c) www.rdtecnologia.com.br
# Licence   : GPL v3
#-------------------------------------------------------------------------------

from retrying import retry
from time import gmtime, strftime
import sys

PY_VERSION = sys.version_info[0]
if PY_VERSION == 3:
    import urllib.request

@retry(wait_random_min=1000, wait_random_max=2000)
def urlopen_with_retry(url, fileToSave):
    if PY_VERSION == 3:
        urllib.request.urlretrieve(url,fileToSave)
    if PY_VERSION == 2:
        wget.download(url, fileToSave)
    print('Try download at :: ' + strftime("%Y-%m-%d %H:%M:%S",gmtime()))
    return True
 	
urlopen_with_retry(sys.argv[1], sys.argv[2])