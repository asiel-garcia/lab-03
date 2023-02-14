import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "05a7c3258f4f81e9335c16d154340b9c"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()
    
response = requests.get('https://official-joke-api.appspot.com/random_joke')
if response.status_code == 200:
	data= response.json()
	for key in data.items():
		print(key)
else:
	print("request failed")
