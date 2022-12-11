# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
import requests

API_KEY = 'f6dafed39ebb95ff314b59fa2ae40800'


def get_weather():
    # city_name
    city_name = 'Kyiv'
    url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"

    response = requests.get(url)
    print(response.json())
