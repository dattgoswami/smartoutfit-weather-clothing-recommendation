# SmartOutfit - Weather Clothing Recommendation with Llama Model

This Python script fetches the weather data for a specified city using the OpenWeatherMap API and then uses the Llama-7b to generate clothing recommendations based on the temperature. The script requires you to have API keys for both the OpenWeatherMap and Llama-7b.

## Prerequisites

Before running the script, you need to obtain API keys for the following services:

1. OpenWeatherMap API: Sign up for an account on [OpenWeatherMap](https://openweathermap.org/) to get your API key.

2. Llama Model API: Sign up for an account on [MonsterAPI](https://monsterapi.ai/) to get your Llama model API key and authentication token.

## Installation

To run this script, you need to have Python 3.x installed on your machine. Additionally, you'll need to install the `requests` library, which can be done using the following command:

```
pip install requests
```

## Usage

1. Replace the placeholders `YOUR_OPEN_WEATHER_MAP_API_KEY`, `YOUR_LLM_API_KEY`, and `YOUR_LLM_AUTH_TOKEN` in the script with your actual API keys.

2. Execute the script:

```
python3 weather_clothing_recommendation.py
```

The script ask for the name of the city, and then will fetch the weather data, convert the temperature to Celsius, and then use the Llama model to generate clothing recommendations based on the temperature. The final clothing recommendation will be printed in the console.

Example Input/Output:

```
Prompt:
The weather today has a temperature of 25°C. What clothes should I wear if I am going out for a walk?
Recommendation:
 Hello! I'm here to help you with your question. However, I must point out that the temperature of 25°C is quite warm and sunny, so it would be best to dress in lightweight and breathable clothing for a walk outside.
Here are some suggestions:
1. Lightweight t-shirt or blouse: A comfortable and breathable top layer will keep you cool and relaxed during your walk.
2. Shorts or skirts: Shorts or skirts are great options for warmer weather as they allow for good airflow and can help keep you cool. Just make sure to choose a pair that is comfortable and suitable for walking.
3. Sunglasses: Protect yourself from the sun's rays by wearing sunglasses. Not only do they look stylish, but they also provide UV protection for your eyes.
4. Comfortable shoes: Choose shoes that are comfortable and supportive, as you'll be on your feet for an extended period. Sandals or sneakers are great options for walks.
Remember to stay hydrated and wear sunscreen if you plan to spend more time outside. Have a lovely day!
```

Please note that the Llama model API may take some time to process the request, so the script will poll for the result until it's ready.

## Disclaimer

This script is intended for educational and informational purposes only. The clothing recommendations provided by the Llama model are generated based on the input data, but they may not always be accurate or suitable for all weather conditions. Use your own judgment and refer to local weather forecasts and recommendations for dressing appropriately. The script does not guarantee any specific results or outcomes.

## License

This script is provided under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.
