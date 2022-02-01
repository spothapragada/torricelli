import pandas as pd
import numpy as np
from apikeys import WEATHER_API_KEY
from datetime import tz_localize

# A dictionary of lat/long coordinates for the cities
cities = {'New York': (40.7128, -74.0059),
          'London': (51.5074, -0.1278),
          'Paris': (48.8566, 2.3522),
          'Rome': (41.9028, 12.4964),
          'Berlin': (52.5200, 13.4050),
          'Madrid': (40.4168, 3.7038),
          'San Mateo': (37.5631, -122.3293),
          'San Francisco': (37.7749, -122.4194),
          'Kansas City': (39.0997, -94.5786),
          }

if '__main__' == __name__:

    # Convert dates to UTC
    df = pd.read_csv('data/weather_data.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')



    data_url = f"https://history.openweathermap.org/data/2.5/history/city?lat={cities['Kansas City'][0]}&lon={cities['Kansas City'][1]}&type=hour&start={'2022-01-30'}&end={'2022-01-31'}&appid={WEATHER_API_KEY}"
    # Get weather data from the URL and store it in a Pandas DataFrame
    weather_data = pd.read_json(data_url)
    # Print the first 5 rows of the DataFrame
    print(weather_data.head())
