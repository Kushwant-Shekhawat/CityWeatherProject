from src.config import GEOCODING_OPEN_METEO_URL, OPEN_METEO_URL, WORLD_BANK_URL
from src.api_client import get_call

def city_details(city_name):
    city_details_params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    city_details_response = get_call(url=GEOCODING_OPEN_METEO_URL, params=city_details_params)
    try:
        city_details = (city_details_response.json())["results"][0]
        if not city_details:
            raise Exception(f"No geocoding results found for city_details.")
        latitude = city_details['latitude']
        longitude = city_details['longitude']
        country_code = f"{(city_details['country_code']).lower()}"
        timezone = f"{city_details['timezone']}"
        population = f"{city_details['population']}"
        city = f"{city_details['name']}"
        return latitude, longitude, country_code, timezone, population, city
    except Exception as e:
        raise Exception(f"Error while fetching city_details : {e}")

def weather_details(latitude, longitude, timezone):
    weather_forecast_params = {"latitude": latitude, "longitude": longitude, "current_weather": True, "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum", "timezone": timezone}
    weather_forecast_response = get_call(url=OPEN_METEO_URL, params=weather_forecast_params)
    try:
        weather_forecast = weather_forecast_response.json()
        if not weather_forecast:
            raise Exception(f"No data found for weather_forecast.")
        timezone_abbreviation = f"{weather_forecast['timezone_abbreviation']}"
        wind_speed = f"{weather_forecast['current_weather']['windspeed']} {weather_forecast['current_weather_units']['windspeed']}"
        wind_direction = f"{weather_forecast['current_weather']['winddirection']}{weather_forecast['current_weather_units']['winddirection']}"
        current_temperature = f"{weather_forecast['current_weather']['temperature']}{weather_forecast['current_weather_units']['temperature']}"
        maximum_temp = f"{max(weather_forecast['daily']['temperature_2m_max'])}{weather_forecast['daily_units']['temperature_2m_max']}"
        minimum_temp = f"{min(weather_forecast['daily']['temperature_2m_min'])}{weather_forecast['daily_units']['temperature_2m_min']}"
        return timezone_abbreviation, wind_speed, wind_direction, current_temperature, maximum_temp, minimum_temp
    except Exception as e:
        raise Exception(f"Error while fetching weather_forecast : {e}")

def country_info(country_code):
    country_info_url = f"{WORLD_BANK_URL}/{country_code}"
    country_info_params = {"format": "json"}
    country_info_response = get_call(url=country_info_url, params=country_info_params)
    try:
        country_info = country_info_response.json()
        if not country_info:
            raise Exception(f"No data found for country_info.")
        name_of_country = f"{country_info[1][0]['name']}"
        capital_city = f"{country_info[1][0]['capitalCity']}"
        return capital_city, name_of_country
    except Exception as e:
        raise Exception(f"Error while fetching country_info : {e}")