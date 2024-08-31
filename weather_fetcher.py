import requests
import config

def fetch_weather():
    url = f"{config.WEATHER_API_URL}/{config.LOCATION}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Weather for {config.LOCATION}: {response.text}")
        else:
            print("Failed to fetch weather data.")
    except Exception as e:
        print(f"An error occurred: {e}")
