import paho.mqtt.client as mqtt
import mysql.connector
import random
import json
import queue
import time
import threading

# Create Queue Handle
q = queue.Queue()

word_Temp = "temp_humid_1"
word_Temp2 = "temp_humid_2" 
word_Light= "Light Sensor(OPZ1ZT)"

broker = 'en-apis.zifisense.com'
port = 1883
topic =  "980f70347bc145c8a0adb4a34a76b264/jll/property/ms/+/updata"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = '980f70347bc145c8a0adb4a34a76b264'
password = 'a7ae992006b5486bbda172e1752303aa'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("MQTT Connected")
        else:
            print("MQTT Not Connect")
    # Set Connecting Client ID
    client = mqtt.Client(client_id,protocol=mqtt.MQTTv31)
    print("Client ID: ",client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        global q
        decoded_text = msg.payload.decode("utf-8")
        #print("decoded_text is ",decoded_text)
        try:
            json_res = json.loads(decoded_text)
         #   print("json is ",json_res)
            q.put(json_res)
        except:
            print("The incoming data is not json!!")
        print(" ------------------------------ ")
        return

    client.subscribe(topic)
    client.on_message = on_message

def insert_data_temp(CompanyCode,DeviceType,Data,Info):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into temphumid(CompanyCode,DeviceType,Data,Info) values(%s,%s,%s,%s)"
    val=(str(CompanyCode),str(DeviceType),str(Data),str(Info))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

def insert_data_light(CompanyCode,DeviceType,Data,Info):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into light(CompanyCode,DeviceType,Data,Info) values(%s,%s,%s,%s)"
    val=(str(CompanyCode),str(DeviceType),str(Data),str(Info))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

def insert_data_tempgrp(DeviceType,Info):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into tempgrp(DeviceType,Info) values(%s,%s)"
    val=(str(DeviceType),str(Info))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

def insert_data_tempgrp2(DeviceType,Info):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into tempgrp2(DeviceType,Info) values(%s,%s)"
    val=(str(DeviceType),str(Info))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

def insert_data_lightgrp(DeviceType,Info):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into lightgrp(DeviceType,Info) values(%s,%s)"
    val=(str(DeviceType),str(Info))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

def processQueueTask(q):
    start = {}
    end = {}
    json_get = ""
    while(1):
        print("-------- processTask ---------")
        try:
            if (q.empty() == True):
                print("No any data is Queue!!")
            else:
                json_get = q.get()
                print("json_get = ",json_get)
                with open('data.text', 'w') as json_file:
                    json.dump(json_get, json_file, indent=4) 
                with open("data.text", "r") as file:
                    for line_number, line in enumerate(file, start=1):  
                        if word_Temp in line:
                            with open('data.text') as fs:
                                data_filter = fs.read()
                                data = json.loads(data_filter)
                                company_data = data['companyCode']
                                print("CompanyCode : ",company_data)
                                device = data['deviceAlias']
                                print("DeviceType : ",device)
                                bit_data_Temphumid1 = data['data']
                                print('Data_Temp1 :',bit_data_Temphumid1)
                                # Decode Bit Temp
                                bit_Temp1 = (bit_data_Temphumid1[2:6])
                                print('Bit_Temp1 :', bit_Temp1)
                                decode_bit_temp1 = int(bit_Temp1,16)*0.1
                                print('Temp1 : %.2f Celsius' %decode_bit_temp1)
                                # Decode Bit Humid
                                bit_humid1 = (bit_data_Temphumid1[6:8])
                                print('Bit Humid1 : ',bit_humid1)
                                decode_bit_humid1 = int(bit_humid1,16)
                                print('Humid1 : {} RH%'.format(decode_bit_humid1))
                                Temp1 = "{:.2f}".format(decode_bit_temp1)
                                Humid1 = decode_bit_humid1
                                Info_temp1 = 'Temp : {} Celcius , Humid : {} RH%'.format(Temp1,Humid1)
                                insert_data_temp(company_data,device,bit_data_Temphumid1,Info_temp1)
                                insert_data_tempgrp(device,Temp1)
                        elif word_Temp2 in line:
                            with open('data.text') as fs:
                                data_filter = fs.read()
                                data = json.loads(data_filter)
                                company_data = data['companyCode']
                                print("CompanyCode : ",company_data)
                                device = data['deviceAlias']
                                print("DeviceType : ",device)
                                bit_data_Temphumid2 = data['data']
                                print('Data_Temp2 :',bit_data_Temphumid2)
                                # Decode Bit Temp
                                bit_Temp2 = (bit_data_Temphumid2[2:6])
                                print('Bit_Temp2 :', bit_Temp2)
                                decode_bit_temp2 = int(bit_Temp2,16)*0.1
                                print('Temp2 : %.2f Celsius' %decode_bit_temp2)
                                # Decode Bit Humid
                                bit_humid2 = (bit_data_Temphumid2[6:8])
                                print('Bit Humid : ',bit_humid2)
                                decode_bit_humid2 = int(bit_humid2,16)
                                print('Humid2 : {} RH%'.format(decode_bit_humid2))
                                Temp2 = "{:.2f}".format(decode_bit_temp2)
                                Humid2 = decode_bit_humid2
                                Info_temp2 = 'Temp : {} Celcius , Humid : {} RH%'.format(Temp2,Humid2)
                                insert_data_temp(company_data,device,bit_data_Temphumid2,Info_temp2)
                                insert_data_tempgrp2(device,Temp2)
                        elif word_Light in line:
                            with open('data.text') as fs:
                                data_filter = fs.read()
                                data = json.loads(data_filter)
                                company_data = data['companyCode']
                                print("CompanyCode : ",company_data)
                                device = data['deviceAlias']
                                print("DeviceType : ",device)
                                bit_data_Light = data['data']
                                print('Data_Light :',bit_data_Light)
                                # Decode Bit Light
                                bit_Light = (bit_data_Light[2:6])
                                print('Bit_Light :', bit_Light)
                                decode_bit_Light = int(bit_Light,16)*0.1
                                print('Light : %.2f lux' %decode_bit_Light)
                                Info_light = 'Illuminance : {:.2f} lux'.format((decode_bit_Light))
                                light = "{:.2f}".format(decode_bit_Light)
                                insert_data_light(company_data,device,bit_data_Light,Info_light)
                                insert_data_lightgrp(device,light)
        except:
            print("Error")
        time.sleep(5) # delay for 5 sec.
    return

worker = threading.Thread(target=processQueueTask, args=(q,), daemon=True) # create python thread (like xTaskCreate in platform IO)
worker.start()

client = connect_mqtt()
subscribe(client)
client.loop_forever()