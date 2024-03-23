import requests
from dotenv import load_dotenv
import os
from pprint import pprint
# Load the .env file 
load_dotenv() 

def get_current_weather():
    print("Get Current Weather")

    city = input("Please send a city name: ")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)
    
    print(f'\nCurrent weather for {city}: ')
    print(f'\nTempreature: {weather_data["main"]["temp"]}')
    print(f'\nFeels like: {weather_data["main"]["feels_like"]}')
    print(f'\nSummary: {weather_data["weather"][0]["description"]}')


if __name__ == '__main__':
    get_current_weather()