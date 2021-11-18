import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message " + str(message.payload.decode("utf-8")) + " on topic " + message.topic)


def sub_fake_data():

    #mqttBroker = "mqtt.eclipseprojects.io"
    mqttBroker = "40.117.213.255"
    client = mqtt.Client("FakeDataReceiver")
    client.username_pw_set('client002', 'unknownwords')
    client.connect(mqttBroker)

    client.loop_start()

    client.subscribe("Fake Data")
    client.on_message = on_message
    time.sleep(120)

    client.loop_end()

if __name__ == '__main__':
    sub_fake_data()
