# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:19:20 2023

@author: Natth
"""

import numpy as np
import json
import paho.mqtt.client as paho
import queue
import threading
import time

# Create Queue Handle
q = queue.Queue()

#----------------------------------------+
#     MQTT function and parameters       |
#----------------------------------------+
scn_topic = "980f70347bc145c8a0adb4a34a76b264/jll/property/ms/4f030b3d/updata"
user = '980f70347bc145c8a0adb4a34a76b264'
password = 'a7ae992006b5486bbda172e1752303aa'
broker_addr = "en-apis.zifisense.com" #"broker.hivemq.com" #"broker.mqttdashboard.com"
port_num = 1883 #8883 #1883
wait_s = 5

# =============================================================================
#           Declare function here
# =============================================================================
def on_subscribe(client, userdata, mid, granted_qos):
    pass
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
    return

def on_message(client, userdata, msg):
    global q
    decoded_text = msg.payload.decode("utf-8")
    print("decoded_text is ",decoded_text)
    try:
        json_res = json.loads(decoded_text)
        print("json is ",json_res)
        q.put(json_res)
    except:
        print("The incoming data is not json!!")
    print(" ------------------------------ ")
    return

# =============================================================================
#               Declare thread here (Like a Task in platform IO)
# =============================================================================

def processQueueTask(q):
    json_get = ""
    while(1):
        print("-------- processTask ---------")
        try:
            if (q.empty() == True):
                print("No any data is Queue!!")
            else:
                json_get = q.get()
                print("json_get = ",json_get)
        except:
            print("Error")
        time.sleep(5) # delay for 5 sec.
    return


# =============================================================================
#               Start main code (Like in void setup() in platform IO)
# =============================================================================
#        threading.Thread(target = <task function>, args = <pass value>, daemon=True)
worker = threading.Thread(target=processQueueTask, args=(q,), daemon=True) # create python thread (like xTaskCreate in platform IO)
worker.start()
      

# ################################################
# #             MQTT Broker Setup               #
# ################################################
keepAlive = 3
rand_client_id = "id" + str(np.random.randint(20000000,30000000))
client = paho.Client(client_id=rand_client_id, clean_session=True)
client.username_pw_set(user, password=password)  # set username and password
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker_addr, port_num, keepAlive, bind_address = "" )
client.subscribe(scn_topic, qos=0)
client.loop_forever()
