import paho.mqtt.client as mqtt
from time import sleep
import os

print("Connecting to broker...")

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
	print("Publishing!")
	for j in range(5):
		client.loop()

client.disconnect()
client.loop_stop()

