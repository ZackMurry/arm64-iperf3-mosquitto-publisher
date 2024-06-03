import paho.mqtt.client as mqtt
from time import sleep
import os

def on_connect(client, userdata, flags, reason_code, properties):
	print(f"Connected with code {reason_code}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
broker_ip = os.environ["BROKER_IP"]
client.connect(broker_ip)

sleep(5)
client.loop()
print("Ready!")

for i in range(1000):
	client.publish("bandwidth", i, qos=2)
	sleep(5)

client.disconnect()
client.loop_stop()

