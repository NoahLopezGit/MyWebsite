import sys
# 'Activate venv' option 1
#sys.path.insert(0,"/path/to/venv/lib/python3.8/site-packages")

# 'Activate venv' option 2
#activate_this = '/path/to/env/bin/activate_this.py'
#with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

# Activate venv option 3 is to pass python-home=/path/to/venv in the WSGIDaemonProcess line 
from my_flask_app import app as application