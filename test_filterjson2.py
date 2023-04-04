def fix_data(data):
    if type(data) is list:
        for i, e in enumerate(data):
            if e is None:
                data[i] = ''
            else:
                fix_data(e)

    elif type(data) is dict:
        for k, v in data.items():
            if v is None:
                data[k] = ''
            else:
                fix_data(v)

# Example:

data = {
    "companyCode": "980f70347bc145c8a0adb4a34a76b264",
    "deviceType": "Temperature And Humidity Sensor(THZ2ZT)",
    "data": "0100f330",
    "deviceAlias": "temp_humid_2",
    "parsedData": {
        "upperThresholdOfTemp": null,
        "alarmCycle": null,
        "heartCycle": null,
        "dataStatus": "normal",
        "clearAlarmThresholdOfTemp": null,
        "completeData": "normal,\u6e29\u5ea6\u503c: 24.3\u2103,\u6e7f\u5ea6\u503c: 48RH%",
        "clearAlarmThresholdOfHum": null,
        "lowerThresholdOfTemp": null,
        "versionNumber": "",
        "alarmType": null,
        "lowerThresholdOfHum": null,
        "clearAlarmType": null,
        "acquisitionCycle": null,
        "upperThresholdOfHum": null,
        "temperature": {
            "unit": "\u2103",
            "name": "\u6e29\u5ea6\u503c",
            "nameEn": "",
            "value": "24.3"
        },
        "header": "01",
        "humidity": {
            "unit": "RH%",
            "name": "\u6e7f\u5ea6\u503c",
            "nameEn": "",
            "value": 48
        },
        "enableStatus": null
    },
    "dataDetail": "{\"upperThresholdOfTemp\":null,\"alarmCycle\":null,\"heartCycle\":null,\"dataStatus\":\"normal\",\"clearAlarmThresholdOfTemp\":null,\"completeData\":\"normal,\u6e29\u5ea6\u503c: 24.3\u2103,\u6e7f\u5ea6\u503c: 48RH%\",\"clearAlarmThresholdOfHum\":null,\"lowerThresholdOfTemp\":null,\"versionNumber\":\"\",\"alarmType\":null,\"lowerThresholdOfHum\":null,\"clearAlarmType\":null,\"acquisitionCycle\":null,\"upperThresholdOfHum\":null,\"temperature\":{\"unit\":\"\u2103\",\"name\":\"\u6e29\u5ea6\u503c\",\"nameEn\":\"\",\"value\":\"24.3\"},\"header\":\"01\",\"humidity\":{\"unit\":\"RH%\",\"name\":\"\u6e7f\u5ea6\u503c\",\"nameEn\":\"\",\"value\":48},\"enableStatus\":null}",
    "pid": "",
    "deviceCode": 46,
    "deviceVersion": 1,
    "deviceId": "4f030b3d",
    "upTime": 1678813220494,
    "deviceaddr": null,
    "accessKey": "",
    "deviceMold": "ms"
}
fix_data(data)
print(data)