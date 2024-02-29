# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


# dev
# broker = 'emqx.dev.inrobot.cloud'
# port = 1883
# deviceId = "dcce9304f4bfa4743b893c01a5d50f0a5"
# deviceSn = "ChuanDai_Site"
# deviceSecretKey = "b68e80e444f04005b507be7a1f5f3be1"
# productId = "pe67b333fd9b34ac58864a1e32c47240c"

# sit
broker = 'emqx.sit.inrobot.cloud'
port = 1883
deviceId = "db92556d52e9248289daaf16e710edaf9"
deviceSn = "ChuanDai_Site"
deviceSecretKey = "e5cddda3acd447be948335b27366a314"
productId = "pac9e2164404e4ebf9ca5c3fd99ca6754"

# demo
# broker = 'broker.emqx.io'
# port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
# client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(deviceId)
    # client = mqtt_client.Client(client_id)
    client.username_pw_set(deviceSn, deviceSecretKey)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# def publish(client):
#     msg_count = 1
#     while True:
#         time.sleep(1)
#         msg = f"messages: {msg_count}"
#         payload = {
#             "Id": time.time(),
#             "Method": "action_reply",
#             "Timestamp": time.time(),
#             "ActionId": "action",
#             "Data": "aaa" 
#         }
#         result = client.publish(topic, payload)
#         # result: [0, 1]
#         status = result[0]
#         if status == 0:
#             print(f"Send `{msg}` to topic `{topic}`")
#         else:
#             print(f"Failed to send message to topic {topic}")
#         msg_count += 1
#         if msg_count > 5:
#             break

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        data = msg.payload.decode()


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
