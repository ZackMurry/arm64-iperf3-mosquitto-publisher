import paho.mqtt.client as mqtt
from time import sleep
import os
import iperf3

print("Connecting to broker...")

def on_connect(client, userdata, flags, reason_code, properties):
	print(f"Connected with code {reason_code}")

def get_bandwidth(ip, port=5201, duration=5):
	client = iperf3.Client()
	client.server_hostname = ip
	client.port = port
	client.duration = duration

	#print(f'Starting test to {ip}:{port} for {duration} seconds...')

	result = client.run()

	if result.error:
		print(f'Error: {result.error}')
		#sys.exit(1)
	return result.sent_Mbps

#	print('Test completed:')
#	print(f'  Server:       {result.remote_host}')
#	print(f'  Port:         {result.remote_port}')
#	print(f'  Duration:     {result.time} seconds')
#	print(f'  Sent:         {result.sent_bytes} bytes')
#	print(f'  Received:     {result.received_bytes} bytes')
#	print(f'  Sent:         {result.sent_Mbps} Mbps')
#	print(f'  Received:     {result.received_Mbps} Mbps')

iperf_ip = os.environ["IPERF_IP"]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
broker_ip = os.environ["BROKER_IP"]
client.connect(broker_ip)

sleep(5)
client.loop()
print("Ready!")

for i in range(1000):
	bandwidth = get_bandwidth(iperf_ip)
	client.publish("bandwidth", bandwidth, qos=2)
	print(f"Publishing {bandwidth}!")
	for j in range(5):
		client.loop()

client.disconnect()
client.loop_stop()

