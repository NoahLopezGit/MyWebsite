import requests
import json

class HueBridge:
    def __init__(self, website_conf_filepath):
        with open(website_conf_filepath,'r') as openfile:
            website_conf = json.load(openfile)
        self.bridge_ip_address = website_conf['hue']['bridge_ip']
        self.hue_application_key = website_conf['hue']['username']
        self.lights = website_conf['hue']['lights']
        self.base_url = f"https://{self.bridge_ip_address}/clip/v2/resource"
        self.header = {"hue-application-key": self.hue_application_key}
        # self.ca_cert_path = "ca_cert_self.pem" #TODO not currently using this
    
    def control_light(self, light_name, body):
        light_id = self.lights[light_name]
        url = self.base_url + f"/light/{light_id}"
        response = requests.put(url, headers=self.header, json=body, verify=False) #TODO fix ssl verification to use ca cert
        return response
    
    def get_light_state(self, light_name):
        light_id = self.lights[light_name]
        url = self.base_url + f"/light/{light_id}"
        response = requests.get(url, headers=self.header, verify=False)
        return response
    
    def get_light_power_status(self, light_name) -> bool:
        response = self.get_light_state(light_name)
        json_obj = json.loads(response.content.decode('utf-8'))
        return json_obj['data'][0]['on']['on']

    def get_light_states(self):
        return {light_id:self.get_light_power_status(light_id) for light_id in self.lights.keys()}

if __name__=='__main__':
    #initialize bridge
    website_conf_filepath = "website_conf.json"
    my_bridge = HueBridge(website_conf_filepath)
    #control light
    # data = {"on": {"on": False}}
    # response = my_bridge.control_light("light1",body=data)
    # print(response.content.decode(encoding='utf=8'))
    # response = my_bridge.get_light_state("light1")
    # print(response.content.decode(encoding='utf-8'))
    # my_bridge.control_light('light1',{'on':{'on':True}})
    # print(my_bridge.get_light_power_status("light1"))
    # my_bridge.control_light('light1',{'on':{'on':False}})
    # print(my_bridge.get_light_power_status("light1"))
    print(my_bridge.get_light_states())
