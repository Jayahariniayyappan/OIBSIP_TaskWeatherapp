**Python Weather App using wttr.in API**.


# 🌦 Simple Python Weather App

A beginner-friendly **command-line weather app** in Python that fetches and displays current weather information for any city using the free **[wttr.in](https://wttr.in)** API — **no API key required**.

## 📌 Features
- Get **current temperature**, **humidity**, and **weather conditions**
- Works for **any city worldwide**
- Uses **JSON API** from wttr.in
- **No signup or API key** needed

## 🚀 How to Run

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
````

### 2. Install required library

Make sure you have Python 3 installed.
Install `requests` if not already installed:

```bash
pip install requests
```

### 3. Run the app

```bash
python weather.py
```

### 4. Example Output

```
Enter city name: Chennai
Temperature: 28°C
Humidity: 75%
Condition: Partly cloudy
```

## 🛠 Code Overview

```python
import requests

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
```

## 📜 How It Works

1. **Takes user input** for the city.
2. **Sends a GET request** to `wttr.in` with `?format=j1` to get JSON.
3. **Checks the status code** (`200` means OK).
4. **Parses JSON** and extracts:

   * `temp_C` → Temperature in Celsius
   * `humidity` → Humidity percentage
   * `weatherDesc` → Short description of weather

## 💡 Why wttr.in?

* Free and public
* No API key needed
* Fast and easy for beginners

## 📄 License

This project is licensed under the MIT License.

