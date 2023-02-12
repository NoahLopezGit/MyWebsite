import os
import openai
import json
import socket
import datetime

debug = True

if debug==False:
    print('DEBUG is ON')
    openai.api_key = json.load(open('/var/www/html/MyWebsite/openai_api_key.json'))['OPENAI_API_KEY']
else:
    openai.api_key = json.load(open('openai_api_key.json'))['OPENAI_API_KEY']

def get_welcome_message(name):
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"create a welcome message for {name}",
                temperature=0.6,
            )
    return response.choices[0]

def create_response(inquiry):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=str(inquiry),
            temperature=0.6,
        )
    return "Noah: " + response.choices[0]['text'].lstrip('>?')

def is_server_down(host, port):
    try:
        s = socket.create_connection((host, port), timeout=2)
        return False
    except socket.error as e:
        return True

class LePotatoDisplayData():
    def __init__(self):
        self.time = 'No Data'
        self.temp = 'No Data'
        self.pressure = 'No Data'