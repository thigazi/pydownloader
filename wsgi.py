from os import chdir,path
chdir(path.dirname(__file__))

import libs,app
from bottle import default_app

application = default_app()