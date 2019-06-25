from os import urandom
from tagio import send_msg
from time import sleep
from datetime import datetime
import base64


if __name__ == "__main__":
    for i in range(1,3):
        payload = b'\x62' + urandom(2)
        print(payload.hex())
        msg = base64.standard_b64encode(payload).decode("utf-8")
        r = send_msg(msg)
        print(r.text)
        print(datetime.now().strftime('%H:%M:%S %d-%m-%Y'))
        print('=======')
        sleep(2)
        