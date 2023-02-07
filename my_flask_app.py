from flask import Flask, render_template, request
import logging
import datetime
import socket

app = Flask(__name__)
debug = False
submission_filename = 'user_submissions.txt'

@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        print('Post request received')
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        with open(submission_filename, 'a') as submission_file:
            submission_file.write(':'.join([name,email,message])+'\n')
        
    return render_template('main.html', user_ip=request.remote_addr)

@app.route("/minecraft")
def minecraft_page():
    if is_server_down('localhost', 25565):
        mc_server_status = "Server is currently down"
    else:
        mc_server_status = "Server is currently up"
    return render_template('minecraft_page.html', mc_server_status=mc_server_status)

import socket

def is_server_down(host, port):
    try:
        s = socket.create_connection((host, port), timeout=2)
        return False
    except socket.error as e:
        return True

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
