import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.environ['api_key']}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_of_days = 8 * forecast_days
    filtered_data = filtered_data[:no_of_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Trichy", 2, "Temperature"))
