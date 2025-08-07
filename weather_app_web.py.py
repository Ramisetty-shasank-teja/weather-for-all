import requests
import pyttsx3
from colorama import init, Fore, Back, Style

# Initialize colorama for terminal colors
init(autoreset=True)

# Speak text aloud
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Simplify weather condition for easy understanding
def simplify_weather(description):
    description = description.lower()
    if "rain" in description:
        return "It may rain. Carry an umbrella or stay indoors."
    elif "cloud" in description:
        return "Sky is cloudy. There may be less sunlight."
    elif "clear" in description:
        return "Sky is clear. Good weather to go out or work in fields."
    elif "thunderstorm" in description:
        return "Thunderstorm is expected. Stay safe and avoid open areas."
    elif "snow" in description:
        return "Snowfall expected. Wear warm clothes."
    elif "haze" in description or "fog" in description:
        return "Foggy or hazy weather. Drive carefully."
    else:
        return "Normal weather conditions. Stay alert and safe."

# Fetch and show weather details
def get_weather(city):
    api_key = "b50a82b519bf1a64077c94d7433aadf9"  # ✅ Your real API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    full_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']

        simple_message = simplify_weather(weather_desc)

        print(Back.YELLOW + Fore.BLACK + f"\n📍 Weather Report for {city.title()}:\n")
        print(Back.CYAN + Fore.BLACK + f"🌡 Temperature: {temp}°C")
        print(Back.MAGENTA + Fore.WHITE + f"💧 Humidity: {humidity}%")
        print(Back.BLUE + Fore.WHITE + f"🌥 Condition: {weather_desc}")
        print(Back.GREEN + Fore.BLACK + f"🌬 Wind Speed: {wind_speed} m/s")
        print(Back.RED + Fore.WHITE + f"\n🗣 Easy Info: {simple_message}\n")

        speak(simple_message)

    else:
        print(Back.RED + Fore.WHITE + "❌ Sorry, I couldn't fetch the weather details.")
        print(Fore.RED + f"Error Code: {response.status_code}")
        print(Fore.RED + f"Response: {response.text}")
        speak("Sorry, I couldn't fetch the weather details.")

# Ask user for input
city = input(Fore.CYAN + "📌 Enter your city name: ")
get_weather(city)


