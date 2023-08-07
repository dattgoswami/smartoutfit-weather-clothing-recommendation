import requests
import json
from time import sleep

# OpenWeatherMap API setup
OWM_API_KEY = "YOUR_OPEN_WEATHER_MAP_API_KEY"
city = "Calgary"  # Replace with your city name

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}"

# Llama model API setup
LLM_API_KEY = "YOUR_LLM_API_KEY"
LLM_AUTHORIZATION = "YOUR_LLM_AUTH_TOKEN"
llm_url = "https://api.monsterapi.ai/apis/add-task"
fetch_url = "https://api.monsterapi.ai/apis/task-status"

headers = {
    "x-api-key": LLM_API_KEY,
    "Authorization": f"Bearer {LLM_AUTHORIZATION}",
    "Content-Type": "application/json",
}

# Fetch weather data
response = requests.get(weather_url)
weather_data = response.json()

# Prepare data for LLM model
weather_desc = weather_data["weather"][0]["description"]
weather_temp = weather_data["main"]["temp"]  # Temperature in Kelvin
# Convert Kelvin to Celsius
celsius_temp = weather_temp - 273.15
celsius_temp_int = int(celsius_temp)

data = {
    "model": "llama2-7b-chat",
    "data": {
        "prompt": f"The weather today has a temperature of {celsius_temp_int}°C. What clothes should I wear, if I am going out for a walk?",
        "top_k": 10,
        "top_p": 0.9,
        "temp": 0.1,
        "max_length": 1000,
        "beam_size": 1
    }
}

# Post to LLM model and get process_id
response = requests.post(llm_url, headers=headers, data=json.dumps(data))
process_id = response.json()["process_id"]

# Polling to get the result from LLM model
status = None
while True:
    response = requests.post(
        fetch_url,
        headers=headers,
        data=json.dumps({
            "process_id": process_id,
        })).json()

    status = response["response_data"]["status"]
    if status not in ("COMPLETED", "FAILED"):
        sleep(2)
    else:
        break

# Print out the result
if status == "COMPLETED":
    print(response["response_data"]["result"]["text"])
else:
    print("Error:", response["response_data"]["result"]["errorMessage"])
