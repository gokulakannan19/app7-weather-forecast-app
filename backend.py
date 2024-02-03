import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={os.environ['api_key']}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    print(get_data("Trichy", 2, "sky"))
