import requests
import json


url = 'https://api.tago.io/data'
device_token_tagio = "YOUR_DEVICE_TOKEN"


def send_msg(data):
    print(data)
    payload = json.dumps({"variable":"altura","value":data,"unit":"cm"})
    headers = {
        'Content-Type': 'application/json',
        'Device-Token': device_token_tagio
    }
    r = requests.post(url, data=payload, headers=headers)
    return r
