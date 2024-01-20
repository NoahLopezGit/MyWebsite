from flask import Flask, render_template, jsonify, request
from flask_method_module import create_response, is_server_down, LePotatoDisplayData
from hue_control_class import HueBridge
import requests
import json

app = Flask(__name__)
debug = False
submission_filename = 'user_submissions.txt'
lepotato_data = LePotatoDisplayData()
my_bridge = HueBridge('website_conf.json')

@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        print('Post request received')
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        with open(submission_filename, 'a') as submission_file:
            submission_file.write(':'.join([name,email,message])+'\n')
        
    return render_template('main.html')

#hue site
@app.route("/hue", methods=('GET',)) 
def hue_page():
    return render_template('hue_control.html')

#api
@app.route("/API/hue/<light_name>", methods=('POST',))
def control_light(light_name):
    body = request.get_json()
    print(body)
    my_bridge.control_light(light_name, body)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/minecraft")
def minecraft_page():
    return render_template('minecraft_page.html')

@app.route("/API/minecraft")
def get_server_status():
    if is_server_down('localhost', 25565):
        mc_server_status = "Server is currently down"
    else:
        mc_server_status = "Server is currently up"
    return json.dumps({"mc_server_status":mc_server_status})

@app.route("/talk_to_me", methods=('GET',))
def contact_page():
    return render_template('contact.html')

@app.route("/API/talk_to_me/<user_input>", methods=('GET',))
def user_response(user_input):
    response = create_response(user_input)
    print(response)
    return jsonify(response=response)

@app.route('/API/lepotato-host', methods=('POST',))
def lepotato_webhost_update():
    if request.method == 'POST':
        request_json = request.get_json()
        lepotato_data.time = request_json['time']
        lepotato_data.temp = request_json['temp']
        lepotato_data.pressure = request_json['pressure']
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/lepotato-display', methods=('GET',))
def get_lepotato_webdisplay():
    return render_template('lepotato_display.html')

@app.route('/API/lepotato-display/<value_id>', methods=('GET',))
def get_lepotato_webdisplay_data(value_id):
    print(value_id, getattr(lepotato_data, value_id))
    return json.dumps({value_id:getattr(lepotato_data, value_id)})

# @app.route('/test')
# def get_test():
#     return render_template('testing.html')

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=80, debug=True)
