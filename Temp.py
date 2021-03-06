# Temp-Monitor-and-Alert
#Temperature monitor I setup for a datacenter to remove the need for manual monitoring or expensive solutions.
#I used a Raspberry Pi, a DHT22 sensor, and python to monitor and alert via email. Once email is sent, it will wait for 15 minutes before sending another one.

import Adafruit_DHT
import time
import datetime
import smtplib

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  if humidity is not None and temperature is not None:
    ft = (temperature * 9/5) + 32
    if (temperature < 22.22):
      print(" ")
      print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(ft, humidity))
      print(st)
    else:
      port = 25
      OHSender = 'TempMonitor@email.com'
      OHReceiver = ['ITDept@email.com']
      OHMessage = """FROM: From Temp Monitor <TempMonitor@email.com>
To: IT Dept <ITDept@email.com>
Subject: Overheating Alert in building XXXXXXX on #th floor

This is an automated alert. The Datacenter on the #th floor of building XXXXXXXXXX is currently overheating.

Can you please turn on the AC unit to prevent hardware failure?

It is currently at Temp={0:0.1f}F Humidity={1:0.1f}%

Please immediately contact ITDept@email.com
Thank you,
Automated Temperature and humidity monitor
      """.format(ft, humidity)
      smtpObj = smtplib.SMTP('mailhost.ITDept.com')
      smtpObj.sendmail(OHSender, OHReceiver, OHMessage)
      print()
      print("successfully sent email")
      print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(ft, humidity))
      time.sleep(900)
  else:
    continue
  time.sleep(3);
