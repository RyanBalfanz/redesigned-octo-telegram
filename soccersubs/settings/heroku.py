import os

from .production import *

DEBUG = bool(os.getenv("DEBUG", str(int(DEBUG))))
