import requests
# import json

def get_weather(city, api_key):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(URL)
    data = response.json()
    # print(json.dumps(data, indent=3))
    if data["cod"] == 200:
        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "wind_speed": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        print("City not found!")
        return None

def main():
    API_KEY = "bd5e378503939ddaee76f12ad7a97608"
    city = input("Enter the city: ")
    weather_info = get_weather(city, API_KEY)

    if weather_info:
        print(
        f"""
    City: {weather_info["city"]}
    Country: {weather_info["country"]}   
    Temperature: {weather_info["temperature"]}
    Pressure: {weather_info["pressure"]}
    Humidity: {weather_info["humidity"]}
    Description: {weather_info["description"]}
    Wind Speed: {weather_info["wind_speed"]}
        """
        )

if __name__ == "__main__":
    main()