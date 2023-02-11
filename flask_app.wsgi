import sys
import logging
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/html/MyWebsite')
sys.path.insert(0,'/var/www/html/MyWebsite/venv/lib/python3.11/site-packages')

from my_flask_app import app as application
application.secret_key = os.getenv('SECRET_KEY')