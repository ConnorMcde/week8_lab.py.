"""Week 8 exercise 7 defensive coding"""

import requests
import datetime
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"#fetch
response = requests.get(url)
data = response.json()

#process
temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]

#Logic: Weather message
if temperature < 10:
    message = "It's cold, wear a coat."
else:
    message = "Nice weather."

#display
print(f"Temperature: {temperature}°C")
print(f"Windspeed: {windspeed} km/h")
print(message)

#Save and Append to weather_log.txt with timestamp
timestamp = datetime.datetime.now()
with open("weather_log.txt", "a") as file:
    file.write(f"{timestamp} | Temp: {temperature}°C | Wind: {windspeed} km/h | {message}\n")