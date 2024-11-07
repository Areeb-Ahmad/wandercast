import requests
import os
from dotenv import load_dotenv
import tkinter

class Weather:
    def __init__(self, tk_canvas: tkinter.Canvas, city: str):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.WINDOW = tk_canvas
        self.CITY = city
        self.URL = f"http://api.openweathermap.org/data/2.5/forecast?q={self.CITY}&appid={self.API_KEY}&units=metric"
        self.WIDTH = self.WINDOW.winfo_width()
        self.HEIGHT = self.WINDOW.winfo_height()

    # Function to get hourly weather forecast data from OpenWeather API
    def get_forecast(self):
        try:
            response = requests.get(self.URL)
            data = response.json()

            if response.status_code == 200:
                # Clear previous weather graphics
                self.WINDOW.delete("weather")
                for index, hour_data in enumerate(data['list'][:4]):  # Next 8 hours of forecast
                    temperature = hour_data['main']['temp']
                    time_stamp = hour_data['dt_txt']

                    x_pos = self.WIDTH // 2   # Adjust spacing as needed
                    y_pos = self.HEIGHT // 2  # Position below time and date

                    # Display temperature and time
                    self.WINDOW.create_text(
                        x_pos, y_pos + 60, text=f"{temperature}°C", tags="weather",
                        fill="black", font=("Helvetica", 20)
                    )
                    self.WINDOW.create_text(
                        x_pos, y_pos + 30, text=time_stamp.split()[1][:5], tags="weather",
                        fill="black", font=("Helvetica", 25, "bold")
                    )
            else:
                print(f"Error: {data.get('message', 'Error fetching weather data')}")
                self.WINDOW.create_text(400, self.HEIGHT // 2,
                                        text="Error fetching weather data",
                                        tags="weather", fill="red")
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
