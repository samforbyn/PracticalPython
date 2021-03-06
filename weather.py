import requests
from requests import api

def getWeather():
    api_key = "ebf0c856026d53572f3dde77ae21d3b1"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")

    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }

def main():
    weather_dict = getWeather()
    # Print the results

    print(f"Todays forecast is {weather_dict.get('description')}")
    print(f"The minimum temperature is {weather_dict.get('temp_min')}")
    print(f"The maximum temperature is {weather_dict.get('temp_max')}")

main()