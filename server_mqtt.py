import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
load_dotenv(".env")


def on_connect(client, userdata, flags, rc):
    client.subscribe("greenhouse/#")


def on_message_temperature(client, userdata, msg):
    print('Received a new temperature data ', str(msg.payload.decode('utf-8')))


def on_message_humidity(client, userdata, msg):
    print('Received a new humidity data ', str(msg.payload.decode('utf-8')))


def on_message_wind(client, userdata, msg):
    print('Received a new wind data ', str(msg.payload.decode('utf-8')))


client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add('greenhouse/temperature', on_message_temperature)
client.message_callback_add('greenhouse/humidity', on_message_humidity)
client.message_callback_add('greenhouse/wind', on_message_wind)


client.username_pw_set(os.environ.get("USERNAME_SERVER"), os.environ.get("PASSWORD_SERVER"))
client.connect(str(os.environ.get("HOST_SERVER")), int(os.environ.get("PORT_SERVER")), 60)
client.loop_start()


while True:
    pass
