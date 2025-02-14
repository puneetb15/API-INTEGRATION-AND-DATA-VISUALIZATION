import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title("Weather Data Dashboard")

# Input for city
city = st.text_input("Enter City Name", "Karnataka")  # Default city is London

# Fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

# Replace with your OpenWeatherMap API key
api_key = "9274b90e9ce2d8d06857de7b03239aa9"

# Fetch weather data
weather_data = fetch_weather_data(city, api_key)

# Display weather data
if weather_data:
    # Extract relevant data
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_description = weather_data['weather'][0]['description']

    # Create a DataFrame for visualization
    data = {
        "Metric": ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Weather Description"],
        "Value": [temperature, humidity, wind_speed, weather_description]
    }
    df = pd.DataFrame(data)

    # Display the data table
    st.write("### Weather Data")
    st.write(df)

    # Create a bar chart
    st.write("### Weather Metrics")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="Metric", y="Value", data=df[df['Metric'] != "Weather Description"], palette="viridis", ax=ax)
    ax.set_title(f"Weather Data for {city}")
    ax.set_ylabel("Value")
    ax.set_xlabel("Metric")
    st.pyplot(fig)

    # Create a pie chart
    st.write("### Weather Description")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie([1], labels=[weather_description], autopct='%1.1f%%', colors=['lightblue'])
    ax.set_title("Weather Description")
    st.pyplot(fig)