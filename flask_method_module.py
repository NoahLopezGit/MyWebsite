import os
import openai
import json

openai.api_key = json.load(open('/var/www/html/MyWebsite/openai_api_key.json'))['OPENAI_API_KEY']

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
