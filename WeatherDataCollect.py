#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request
import json
import mysql.connector
import requests

url='https://v0.yiketianqi.com/api?version=v61&appid=46483663&appsecret=ed67oe22&city=长沙'
rep = requests.get(url)
#print('返回结果:%s'%rep.json())
req_jason = rep.json()
date_now = req_jason['date']
city_name = req_jason['city']
update_time = req_jason['update_time']
wea = req_jason ['wea']

tem_now = req_jason['tem']
tem_max = req_jason['tem1']
tem_min = req_jason['tem2']
win  = req_jason['win']

win_speed = req_jason['win_speed']
humidity = req_jason['humidity']
pressure = req_jason['pressure']
air = req_jason['air']

air_level = req_jason['air_level']
alarm_type = req_jason['alarm']['alarm_type']
alarm_level = req_jason['alarm']['alarm_level']
alarm_content = req_jason['alarm']['alarm_content']

print(date_now)
print(city_name)

mydb = mysql.connector.connect(host='127.0.0.1',
    user='root',
    passwd='123',
    database='countrydb')

mycursor = mydb.cursor()
sql = "INSERT INTO weather_data_now (date_now, city_name, update_time, wea, tem_now, tem_max, tem_min, win, win_speed,humidity, pressure, air, air_level, alarm_type, alarm_level, alarm_content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (date_now, city_name, update_time, wea, tem_now, tem_max, tem_min, win, win_speed, humidity, pressure, air, air_level, alarm_type, alarm_level, alarm_content)
mycursor.execute(sql, val)
mydb.commit()
#print(mycursor.rowcount, " 条已经插入")



