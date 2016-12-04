#!/usr/bin/python

import sys, os, crypto
NEW_PATH = "/usr/local/lostexhaust/lostexhaust/api"
if not NEW_PATH in sys.path:
    sys.path.append(NEW_PATH)
NEW_PATH = "/usr/local/lostexhaust/lostexhaust/api/lostexhaust"
if not NEW_PATH in sys.path:
    sys.path.append(NEW_PATH)
sys.modules['Crypto'] = crypto

from lostexhaust.routes import api
from lostexhaust import app as application

