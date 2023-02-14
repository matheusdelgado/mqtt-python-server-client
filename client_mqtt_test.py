import os
import time
import random
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
load_dotenv(".env")

mqttClient = mqtt.Client(client_id="greenhouse")
mqttClient.connect(str(os.environ.get("HOST_SERVER")), int(os.environ.get("PORT_SERVER")))
mqttClient.loop_start()


def update_numbers():
    return {
        "temperature": random.randint(0, 50),
        "humidity": f"{random.randint(0, 100)}%",
        "wind": f"{random.randint(0, 300)}km/h"
    }


while True:
    msg = update_numbers()
    info = mqttClient.publish(
        topic='greenhouse/temperature',
        payload=msg.get("temperature"),
        qos=0,
    )
    info = mqttClient.publish(
        topic='greenhouse/humidity',
        payload=msg.get("humidity").encode('utf-8'),
        qos=0,
    )
    info = mqttClient.publish(
        topic='greenhouse/wind',
        payload=msg.get("wind").encode('utf-8'),
        qos=0,
    )
    info.wait_for_publish()
    print(info.is_published())
    time.sleep(3)
