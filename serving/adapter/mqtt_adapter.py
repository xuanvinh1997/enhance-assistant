import logging

from paho.mqtt import client as mqtt_client

from serving.adapter import Adapter



class MQTTAdapter(Adapter):
    def __init__(self, broker, port, topic, client_id):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.client = None
    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # override
    def connect(self, on_connect):

        self.client = mqtt_client.Client(self.client_id)
        # self.client.username_pw_set(username, password)
        if on_connect:
            self.client.on_connect = on_connect
        else:
            self.client.on_disconnect = self.__on_connect

        try:
            self.client.connect(self.broker, self.port)
        except Exception as e:
            print(f"Failed to connect to MQTT Broker, error: {e}")
            return None

        return self.client

    def subscribe(self, on_message):
        # def on_message(client, userdata, msg):
        #     print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self.client.subscribe(self.topic)
        self.client.on_message = on_message
