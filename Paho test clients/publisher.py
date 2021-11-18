import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

def pub_fake_data():

    #mqttBroker = "68.58.61.2"
    mqttBroker = "40.117.213.255"
    #mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("FakeDataFeeder")
    client.username_pw_set('client001', 'topsecret')
    client.connect(mqttBroker, port=1883)

    while 1:
        data = uniform(0,100)
        client.publish("Fake Data", data)
        print("Publisher sent: " + str(data) + " to topic Fake Data")
        time.sleep(1)


if __name__ == '__main__':
    pub_fake_data()
