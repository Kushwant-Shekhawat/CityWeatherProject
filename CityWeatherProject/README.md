
# CityWeatherProject 🌦️🌍  
A simple Python CLI project that takes a **city name** as input, fetches **geocoding + weather + country details** using public APIs, and prints a clean weather report in the terminal.

> Author: Kushwant  
> Tech: Python, requests, REST APIs, JSON parsing

---

## ✅ Features
- Takes user input using `input()`
- Fetches city **latitude/longitude**, **timezone**, and **population** using **Open-Meteo Geocoding API**
- Fetches **current weather**, **wind**, and **daily max/min temperatures** using **Open-Meteo Weather Forecast API**
- Fetches **country name** and **capital city** using **World Bank Country API**
- Uses a centralized API call helper (`api_client.py`) with timeout handling
- Strict validation:
  - City name cannot be empty
  - City name cannot be numeric
  - City name spelling must match the returned city name from API (strict requirement)

---

## 🧠 How it works (Flow)
1. User enters `city_name`
2. `city_details(city_name)` → returns:
   - latitude, longitude, country_code, timezone, population, city
3. Strict spelling check:
   - If `city_name.lower() != city.lower()`, raise error (requirement)
4. `weather_details(latitude, longitude, timezone)` → returns weather info
5. `country_info(country_code)` → returns country details
6. Prints final report

---

## 🌐 APIs Used
### 1) Open-Meteo Geocoding API (City → lat/lon)
- Base URL: `https://geocoding-api.open-meteo.com/v1/search`

### 2) Open-Meteo Forecast API (lat/lon → weather)
- Base URL: `https://api.open-meteo.com/v1/forecast`

### 3) World Bank Country API (country_code → country details)
- Base URL: `https://api.worldbank.org/v2/country`

---

## 📦 Run the Project
python main.py

## Then enter city name when prompted:
Enter city name: London

## 🧾 Example Output

===== Weather Report by Kushwant =====
City Name                : LONDON
Coordinates              : [51.5072, -0.1276]
City Population          : 8961989
Country Name             : UNITED KINGDOM
Capital City             : LONDON
Timezone Name            : Europe/London
Time Offset              : GMT+0
Temperature              : 7.3°C
Today's Max. Temperature : 11.0°C
Today's Min. Temperature : 2.0°C
Wind Speed               : 10.5 km/h
Wind Direction           : 280°


## 🔧 Troubleshooting
1) API call fails :
Check internet connection
Try increasing DEFAULT_TIMEOUT in config.py

2) Strict spelling error :
Re-enter the city name with more precise spelling
(Example: "New Delhi" instead of "Delhi")

## 📜 License
This project is for learning purposes. APIs used belong to their respective providers.