import requests  #import request and date time module
from datetime import datetime
import sys
api_key = "a83d006aae78792436c12c223d7a709e"  #api key is required to access the service of particular weather api
city = input("Enter the city: ") # to find the weather forecast of a particular city
full_apiLink = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&" "appid=" + api_key  #in api link we need to link weather api,city, api key
respo = requests.get(full_apiLink) #requests to access the whole apilink
con = respo.json()
if con["cod"] == "404":  #if requests get return 404 then it means page or city not found
    print("Sorry, City was not found")
else:
    ab = con["main"] #we will store all the stuff in main
    cur_temp = (ab["temp"])-273 #since api gives temp in kelsius, so we will subtract to 273
    cur_press = ab["pressure"] #the pressure gives in hPa unit
    cur_hum = ab["humidity"] #the humidity gives in percentage
    wind_speed = con['wind']['speed']
    y = con["weather"]
    WeathDesc = y[0]["description"] #gives the whole weather description
    today = datetime.now().strftime("%d %B %Y | %I:%M:%S %p")  #gives the present time and date

    sys.stdout = open("Weather.txt", "w+")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Weather Report for City - {}||{}".format(city, today))
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\n Temperature (in degree celsius)= ", str(cur_temp))
    print("\n Atmospheric Pressure (in hPa unit) = ", str(cur_press))
    print("\n Wind speed in km/hr is = ", str(wind_speed))
    print("\n Humidity in percentage= ", str(cur_hum))
    print("\n Description = ", str(WeathDesc))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
    sys.stdout.close()   # i use sys module to display all the stuff and print in a text file
#i have used this program 12 times, and it works fine
#Created BY Avinash Soy, IIITDM Jabalpur (2nd year Student)
#after executing it, search weather.txt and check the data written on it
