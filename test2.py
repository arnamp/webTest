import mysql.connector
import json

def insert_data_temp(CompanyCode,DeviceType,Data,Info_data):
   #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
    vibra_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="240901",
        database = "vibra_db"
    )

    db_cursor = vibra_db.cursor()

    sql = "insert into temptest(id,Info) values(%s,%s)"
    val=(str(id),str(Info1))
    db_cursor.execute(sql,val)

    vibra_db.commit()
    vibra_db.close()

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
  Temp1 = round(decode_bit_temp1,2)
  Humid1 = decode_bit_humid1
  Info1 = 'Temp : {} Celcius , Humid : {} RH%'.format(Temp1,Humid1)
  insert_data_temp(company_data,device,bit_data_Temphumid1,Info1)