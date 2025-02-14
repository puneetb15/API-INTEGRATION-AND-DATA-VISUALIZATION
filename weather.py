import requests  # To connect to the API
import pandas as pd  # To create a table

# Step 1: Replace this with your OpenWeatherMap API key
api_key = "9274b90e9ce2d8d06857de7b03239aa9"
city = "Karnataka"  # The city you want weather data for

# Step 2: Define the API URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Step 3: Fetch data from the API
def fetch_weather_data(city, api_key):
    # Build the full URL with the city and API key
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    # Send a request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the data in JSON format
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

# Step 4: Fetch weather data for the city
weather_data = fetch_weather_data(city, api_key)

# Step 5: Extract and organize the data
if weather_data:
    # Extract the information you need
    temperature = weather_data['main']['temp']  # Temperature in Celsius
    humidity = weather_data['main']['humidity']  # Humidity in percentage
    wind_speed = weather_data['wind']['speed']  # Wind speed in m/s
    weather_description = weather_data['weather'][0]['description']  # Weather description (e.g., "clear sky")

    # Step 6: Store the data in a table (DataFrame)
    data = {
        "Metric": ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Weather Description"],
        "Value": [temperature, humidity, wind_speed, weather_description]
    }
    df = pd.DataFrame(data)

    # Step 7: Display the table
    print(df)

    import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a bar chart for temperature, humidity, and wind speed
plt.figure(figsize=(10, 6))  # Set the size of the chart
sns.barplot(x="Metric", y="Value", data=df[df['Metric'] != "Weather Description"], palette="viridis")
plt.title(f"Weather Data for {city}")  # Add a title
plt.ylabel("Value")  # Label for the y-axis
plt.xlabel("Metric")  # Label for the x-axis
plt.show()  # Display the chart

# Step 2: Create a pie chart for weather description
weather_desc = df[df['Metric'] == "Weather Description"]['Value'].values[0]
plt.figure(figsize=(6, 6))  # Set the size of the chart
plt.pie([1], labels=[weather_desc], autopct='%1.1f%%', colors=['lightblue'])
plt.title("Weather Description")  # Add a title
plt.show()  # Display the chart