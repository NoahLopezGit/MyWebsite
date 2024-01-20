import requests
import json

class HueBridge:
    def __init__(self, website_conf_filepath):
        with open(website_conf_filepath,'r') as openfile:
            website_conf = json.load(openfile)
        self.bridge_ip_address = website_conf['hue']['bridge_ip']
        self.hue_application_key = website_conf['hue']['username']
        self.lights = website_conf['hue']['lights']
        self.base_url = f"https://{self.bridge_ip_address}/clip/v2/resource/"
        # self.ca_cert_path = "ca_cert_self.pem" #TODO not currently using this
    
    def control_light(self, light_name, body):
        light_id = self.lights[light_name]
        url = self.base_url + f"/light/{light_id}"
        headers = {"hue-application-key": self.hue_application_key}
        response = requests.put(url, headers=headers, json=body, verify=False) #TODO fix ssl verification to use ca cert
        return response


if __name__=='__main__':
    #initialize bridge
    website_conf_filepath = "website_conf.json"
    my_bridge = HueBridge(website_conf_filepath)
    #control light
    data = {"on": {"on": False}}
    response = my_bridge.control_light(light_id="a7b863de-bce8-4933-86c2-34c8ade5cb79",body=data)
    print(response.content.decode(encoding='utf=8'))