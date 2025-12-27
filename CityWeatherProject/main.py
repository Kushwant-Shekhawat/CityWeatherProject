from src.services import city_details, weather_details, country_info

def main():
    try:
        city_name = input("Enter city name: ").strip()
        if city_name.isnumeric() or not city_name:
            raise ValueError("City Name must be a string!")
        print("You entered:", city_name)
        latitude, longitude, country_code, timezone, population, city = city_details(city_name)
        if city_name.lower() != city.lower():
            raise ValueError(f"Please check the spelling of City Name again and re-enter.! You entered: {city_name}")
        timezone_abbreviation, wind_speed, wind_direction, current_temperature, maximum_temp, minimum_temp = weather_details(latitude, longitude, timezone)
        capital_city, name_of_country = country_info(country_code)

        print("\n===== Weather Report by Kushwant =====")
        print(f"City Name                : {city_name.upper()}")
        print(f"Coordinates              : [{latitude}, {longitude}]")
        print(f"City Population          : {population}")
        print(f"Country Name             : {name_of_country.upper()}")
        print(f"Capital City             : {capital_city.upper()}")
        print(f"Timezone Name            : {timezone}")
        print(f"Time Offset              : {timezone_abbreviation}")
        print(f"Temperature              : {current_temperature}")
        print(f"Today's Max. Temperature : {maximum_temp}")
        print(f"Today's Min. Temperature : {minimum_temp}")
        print(f"Wind Speed               : {wind_speed}")
        print(f"Wind Direction           : {wind_direction}")
    except Exception as e:
        print(f"Error while fetching Details : {e}. You entered: {city_name}")

if __name__ == "__main__":
    main()
