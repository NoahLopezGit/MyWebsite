from flask import Flask, render_template, request
import logging
import datetime

app = Flask(__name__)
debug = False

@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        print('Post request received')
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        with open(submission_filename, 'a') as submission_file:
            submission_file.write('\n'.join([name,email,message])+'\n')
            submission_file.write('\n')
        
    return render_template('main.html', user_ip=request.remote_addr)

@app.route("/minecraft")
def minecraft_page():
    return render_template('minecraft_page.html')
    
if __name__ == "__main__":
    if debug:
        logging.basicConfig(filename = f"C:\\startup_handling\\web_logs\\{datetime.datetime.now().strftime('%Y%m%d%H%M')}_webserver.log", level=logging.DEBUG, format = f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")
        submission_filename = f"C:\\startup_handling\\web_submissions\\{datetime.datetime.now().strftime('%Y%m%d%H%M')}_web_submissions.txt"
    app.run(host='0.0.0.0', port=80, debug=True)
