#!venv/bin/python
activate_this = '/var/www/flaskApp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/flaskApp')

from app import app as application

application.sercret_key = 'you-will-never-guess'
