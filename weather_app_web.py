import streamlit as st
import requests
from gtts import gTTS
import os

st.set_page_config(page_title="Weather For All", page_icon="⛅")
st.title("🌦️ Weather For All")
st.write("Enter a city to get weather info, or type anything to hear it out loud.")

# Section 1: Get Weather Info and Speak it
st.header("📍 Weather Info")
city = st.text_input("Enter city name to get weather")

if st.button("Get Weather"):
    if city:
        api_key = "your_openweather_api_key"  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = f"Weather in {city.title()}:\nTemperature: {temp}°C\nDescription: {desc}\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
            st.success(result)

            # Convert weather info to speech
            tts = gTTS(result)
            tts.save("weather.mp3")
            with open("weather.mp3", "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
        else:
            st.error("City not found. Please check the name.")
    else:
        st.warning("Please enter a city name.")

# Section 2: Custom Text-to-Speech
st.header("🗣️ Speak Your Own Text")
text = st.text_input("Enter text to speak:")

if st.button("Convert to Speech"):
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")

        with open("output.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
    else:
        st.warning("Please enter some text.")
