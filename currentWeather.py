# import required modules
import requests 
import json
import geocoder
import cv2
import numpy as np
import config

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

geodata = geocoder.ip('me').json

# Give city name
city_name = geodata['city']

# complete_url variable to store
# complete url address
city_data_request = base_url + "appid=" + config.weather_key + "&q=" + city_name

# get method of requests module
# return response object
city_data = requests.get(city_data_request).json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if city_data["cod"] == "404":
	print("City Not Found")
	exit()

# store the value of "main"
# key in variable y
data_object = json.dumps(city_data, indent=4)
 
# Writing to sample.json
with open("sampledata.json", "w") as outfile:
    outfile.write(data_object)

# store the value of "weather"
# key in variable z
weather_data = city_data["weather"][0]

# store the value corresponding
# to the "description" key at
# the 0th index of z
weather_main = weather_data["main"]

# print following values
print("Weather for Austin Today: " + str(weather_main))

cap = cv2.VideoCapture('ezgif.com-gif-to-mp4.mp4')

# Read until video is completed
while(cap.isOpened()):
      
# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Poke-weather', frame)
          
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
