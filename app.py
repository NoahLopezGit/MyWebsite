import os, json
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
# from minecraft_server_interface import is_server_down
# from openai_chat import get_open_ai_key, create_response
# from hue_control import HueBridge
# from lepotato_interface import LePotatoDisplayData

#setup
load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

website_directory = os.path.dirname(__file__)
website_conf_filepath = os.path.join(website_directory,'website_conf.json')
submission_filename = os.path.join(website_directory,'user_submission.txt')
# lepotato_data = LePotatoDisplayData()
# my_bridge = HueBridge(website_conf_filepath)
# get_open_ai_key(website_conf_filepath) #TODO fix this, access method deprecated

#Sites
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

@app.route("/hue", methods=('GET',)) 
def hue_page():
    return render_template('hue_control.html')

@app.route("/minecraft")
def minecraft_page():
    return render_template('minecraft_page.html')

@app.route("/talk_to_me", methods=('GET',)) #TODO fix this page, access method deprecated.
def contact_page():
    return render_template('contact.html')

@app.route('/lepotato-display', methods=('GET',))
def get_lepotato_webdisplay():
    return render_template('lepotato_display.html')

@app.route('/test')
def get_test():
    return render_template('testing.html')

#API
# @app.route("/API/hue/<light_name>", methods=('POST',))
# def control_light(light_name):
#     body = request.get_json()
#     print(body)
#     my_bridge.control_light(light_name, body)
#     return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

# @app.route("/API/hue/light-states", methods=('GET',))
# def get_light_power_states():
#     power_states = my_bridge.get_light_states()
#     return json.dumps(power_states)

# @app.route("/API/minecraft")
# def get_server_status():
#     if is_server_down('localhost', 25565):
#         mc_server_status = "Server is currently down"
#     else:
#         mc_server_status = "Server is currently up"
#     return json.dumps({"mc_server_status":mc_server_status})

# @app.route("/API/talk_to_me/<user_input>", methods=('GET',))
# def user_response(user_input):
#     response = create_response(user_input)
#     print(response)
#     return jsonify(response=response)

# @app.route('/API/lepotato-host', methods=('POST',))
# def lepotato_webhost_update():
#     if request.method == 'POST':
#         request_json = request.get_json()
#         lepotato_data.time = request_json['time']
#         lepotato_data.temp = request_json['temp']
#         lepotato_data.pressure = request_json['pressure']
#     return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

# @app.route('/API/lepotato-display/<value_id>', methods=('GET',))
# def get_lepotato_webdisplay_data(value_id):
#     print(value_id, getattr(lepotato_data, value_id))
#     return json.dumps({value_id:getattr(lepotato_data, value_id)})


if __name__ == "__main__":
    app.run()
