import datetime, time, json 
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_connection import CounterFitConnection
import paho.mqtt.client as mqtt

# Virtual Raspberry initialization
CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

# MQTT broker
id = 'loraDevice1'
client_name = id + '_client'
broker_host = 'broker.emqx.io'
broker_port = 1883
# Topics 
title = 'Network statistics for {}'.format(client_name)
network_topic = '/stats/health/'+ client_name +'/network'
# Network
lost_connection = got_connection = ''
reconnect_delay = 3
retries = 0
connected = False

# MQTT event handlers
def on_connect(client, userdata, flags, rc):
    global got_connection, connected
    if rc == 0:
        print('Connected to MQTT broker!')
        got_connection = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        connected = True
    else:
        print('Failed to connect to MQTT broker')

def on_disconnect(client, userdata, rc):
    global lost_connection, connected
    print('Disconnected from MQTT broker!')
    lost_connection = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    connected = False
        
# Set up MQTT client and connect to broker
client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(broker_host, broker_port)

while True:
    client.loop() 
    # Topic message to publish in JSON format
    network_message = {'Time got connection': got_connection, 'Time lost connection': lost_connection, 'Retries': retries} 
    # View local device messages
    print(network_message)
    client.publish(network_topic, json.dumps(network_message))
    # Retry segment
    if not connected:
        try:
            time.sleep(reconnect_delay)
            retries = retries + 1
            client.reconnect()
        except:
            print(f'Reconnection attempt {retries} failed')
    time.sleep(1)
