import paho.mqtt.client as mqtt
from tagio import send_msg


url = "broker_url"
porta = 0
login = "username"
senha = "pass"

def on_connect(client, userdata, flags, rc):
    client.subscribe("topic/+/#")

def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))
    send_msg(msg.payload)
    print(payload.hex())
    r = send_msg(payload)
    print(r.text)
    print(datetime.now().strftime('%H:%M:%S %d-%m-%Y'))
    print('=======')

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set(login, password = senha)
    client.connect(url, porta, 5)
    client.loop_forever()
