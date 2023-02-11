#!/opt/FlaskApp/FlaskApp/venv python3

import sys
import logging
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/opt/FlaskApp/FlaskApp')

from my_flask_app import app as application
application.secret_key = os.getenv('SECRET_KEY')
