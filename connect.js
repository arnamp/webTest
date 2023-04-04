const mysql = require('mysql');
const fs = require('fs');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '240901',
  database: 'vibra_db'
});

connection.connect((error) => {
  if(error){
    console.log('Error connecting to the MySQL Database');
  }
  console.log('Connection MySQL Database Successfully');
});

connection.query('select CompanyCode,DeviceType,Data,Info,Uptime,DATE_FORMAT(temphumid.Uptime, "%W %Y-%m-%d %H:%i:%s") as FormatUptime from temphumid union all select CompanyCode,DeviceType,Data,Info,Uptime,DATE_FORMAT(light.Uptime, "%W %Y-%m-%d %H:%i:%s") as FormatUptime from light order by Uptime desc limit 20',(err, results) => {
  if (err) 
  {
    console.log('error',err);
  }
  console.log(results);
    fs.writeFile('data.json',JSON.stringify(results,null,4),(err)=>{
      if(err) throw err;
      else{
        console.log('Saved!! All Data')
      }
    })
});

connection.query('select DeviceType,Info,Uptime,DATE_FORMAT(temphumid.Uptime,"%W %Y-%m-%d %H:%i:%s") as FormatUptime from temphumid where DeviceType="temp_humid_1" order by Uptime desc limit 1',(err, results) => {
  if (err) 
  {
    console.log('error',err);
  }
  console.log(results);
    fs.writeFile('data_temp1_new.json',JSON.stringify(results,null,4),(err)=>{
      if(err) throw err;
      else{
        console.log('Saved!! TempHumid_1 Data')
      }
    })
});

connection.query('select DeviceType,Info,Uptime,DATE_FORMAT(temphumid.Uptime,"%W %Y-%m-%d %H:%i:%s") as FormatUptime from temphumid where DeviceType= "temp_humid_2" order by Uptime desc limit 1',(err, results) => {
  if (err) 
  {
    console.log('error',err);
  }
  console.log(results);
    fs.writeFile('data_temp2_new.json',JSON.stringify(results,null,4),(err)=>{
      if(err) throw err;
      else{
        console.log('Saved!! TempHumid_2 Data')
      }
    })
});

connection.query('select DeviceType,Info,Uptime,DATE_FORMAT(light.Uptime,"%W %Y-%m-%d %H:%i:%s") as FormatUptime from light order by Uptime desc limit 1',(err, results) => {
  if (err) 
  {
    console.log('error',err);
  }
  console.log(results);
    fs.writeFile('data_light_new.json',JSON.stringify(results,null,4),(err)=>{
      if(err) throw err;
      else{
        console.log('Saved!! Light Data')
      }
    })
});

connection.end((error)=>{
});

