import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
import time


def on_message(client, userdata, message):
    try:
        print ("request recieved at server")
        print (message.payload)
        resopnse_topic = message.properties.ResponseTopic
        client.publish(resopnse_topic, 'server message',1, properties=message.properties)
        print ('response sent from server')
    except:
        print('error')


broker_address = 'localhost'

client = mqtt.Client("server", protocol=mqtt.MQTTv5)
client.connect(broker_address)

client.subscribe('common', options=SubscribeOptions(noLocal=True))

client.on_message = on_message
client.loop_start()
time.sleep(10)  # wait
client.loop_stop()  # stop the loop
