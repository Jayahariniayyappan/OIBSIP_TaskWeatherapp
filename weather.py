
import requests

#Using OpenWeatherMap → API key is required.
#Using wttr.in → API key is not required.


city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current = data["current_condition"][0]
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Condition: {current['weatherDesc'][0]['value']}")
else:
    print("Could not retrieve weather data.")
