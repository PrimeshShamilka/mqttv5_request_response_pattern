import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time

def on_message(client, userdata, message):
    print ('response received at client')
    print (message.payload)

broker_address = 'localhost'

client = mqtt.Client("client", protocol=mqtt.MQTTv5)
client.connect(broker_address)
client.on_message = on_message

# subscribe to response topic
client.subscribe('response')

# request
publish_properties = Properties(PacketTypes.PUBLISH)
publish_properties.ResponseTopic = 'response'
publish_properties.CorrelationData = b"334"

client.publish('common', "client message", 1, properties=publish_properties)
print ('request sent from client')

client.loop_start()
time.sleep(20)  # wait
client.loop_stop()  # stop the loop
