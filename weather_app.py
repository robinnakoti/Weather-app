import requests

def get_weather(city):
    api_key = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "YOUR_API_KEY"  # Replace this with your own API key
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(api_key, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"\n❌ Error: {data.get('message', 'Failed to fetch weather data.')}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)