import datetime
import time
import requests
import json


date = datetime.datetime.now().date().strftime("%d/%m/%Y")
year = int(date.split('/')[2])
month = int(date.split('/')[1])
day = int(date.split('/')[0])

lat = float(input("Enter latitude:"))
lon = float(input("Enter longitude:"))
api_key = "a7b0b2c21ef1f3daa2205b611aecffd6"

pressure_value = []
#Gets past 3 dates
for i in range(day-1, day-4, -1):
    mydatetime = datetime.datetime(year, month, i, 4, 00)
    #Converts datetime to unix time stamp
    Unix_Time_stamp = int(time.mktime(mydatetime.timetuple()))
    #print("Unix_Time_stamp for ",i,': ', Unix_Time_stamp)
    dt = Unix_Time_stamp

    url = 'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%s&lon=%s&dt=%s&appid=%s' % (lat, lon, dt, api_key)

    response = requests.get(url)
    data = json.loads(response.text)
    print('----------------------------------------------------------------------------------')
    print("pressure for",year,'/',month,'/',i,': ',data["current"]["pressure"])
    pressure_value.append(data["current"]["pressure"])
    # print(data)

