#/usr/bin/env

import requests
import os
import tkinter

class Departure:
	def __init__(self,tk_canvas:tkinter.Canvas, city:str):
		load_dotenv()
		self.API_KEY = os.getenv("SL_API_KEY")
		self.WINDOW = tk_canvas
		self.DepartFrom = "DEPARTURE STOP"
		self.Destination = "DESTINATION STOP" 
		self.URL =  "someurl"
		self.HEIGHT = self.WINDOW_winfo_height()
		self.WIDTH = self.WINDOW_winfo_width()

	def get_departure(self):
		try:
			response = requests.get(self.URL)
			data = response.json()

			if response.status_code == 200:
				self.WINDOW.delete("Departures")


#JUST TESTING
