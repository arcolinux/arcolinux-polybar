#!/bin/python
# -*- coding: utf-8 -*-

# Procedure
# Surf to https://openweathermap.org/city
# Fill in your CITY
# e.g. Antwerp Belgium
# Check url
# https://openweathermap.org/city/2803138
# you will the city code at the end
# create an account on this website
# create an api key (free)
# LANG included thanks to krive001 on discord


import requests, time, calendar

CITY = "3094802"
API_KEY = "756edce7e9d4c385ef9499a53492678c"
UNITS = "Metric"
UNIT_KEY = "C"
#UNIT_KEY = "F"
# LANG = "en"
LANG = "pl"
#LANG = "nl"
#LANG = "hu"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        ID = int(REQ.json()["weather"][0]["id"])
        SUNSET = REQ.json()["sys"]["sunset"]
        SUNRISE = REQ.json()["sys"]["sunrise"]
        CURRENT_TIME = calendar.timegm(time.gmtime())
        
        #GROUP 2XX: THUNDERSTORM       
        if ID >= 200 and ID < 300:
            ID_FA = ""
        #GROUP 3XX: DRIZZLE 
        elif ID >= 300 and ID < 400:
            ID_FA = ""
        #GROUP 5XX: RAIN
        elif ID >= 500 and ID < 600:
            ID_FA = ""
        #GROUP 6XX: SNOW
        elif ID >= 600 and ID < 700:
            ID_FA = ""
        #GROUP 7XX: ATMOSPHERE
        elif ID >= 700 and ID < 800:
            ID_FA = ""
        #GROUP 80X: CLOUDS
        elif ID > 800 and ID < 900:
            if ID == 801:
                #DAY
                if CURRENT_TIME >= SUNRISE and CURRENT_TIME <= SUNSET:
                    ID_FA = ""
                #NIGHT
                else:
                    ID_FA = ""
            else:
                ID_FA = ""
        #GROUP 800: CLEAR
        elif ID == 800:
            #DAY
            if CURRENT_TIME >= SUNRISE and CURRENT_TIME <= SUNSET:
                ID_FA = ""
            #NIGHT
            else:
                ID_FA = ""
        else:
            ID_FA = " "
        print("{} {}, {} °{}".format(ID_FA, CURRENT , TEMP, UNIT_KEY))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable to print the data")
