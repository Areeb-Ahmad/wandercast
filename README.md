# wandercast
A Tkinter-based desktop display application that combines a random walker animation with real-time date, time, and weather forecasts.


# WanderCast

**WanderCast** is a Python-based desktop display application using Tkinter that combines a dynamic random walker animation with real-time date, time, and weather forecast. This app is designed to run continuously, providing an eye-catching display of local weather and current time while offering an entertaining random walker visual. Perfect for repurposing an old machine into a beautiful display clock.

## Features
- **Random Walker Animation**: A unique animated walker that moves around the screen within defined boundaries.
- **Real-Time Clock and Date**: Displays the current date and time, updated every second.
- **Weather Forecast**: Fetches and displays hourly temperature forecasts using the OpenWeather API.
- **Fullscreen Mode**: Launches in fullscreen, making it an ideal choice for a dedicated display setup.

## Screenshots
This is an example of the program in action:
![WanderCast Screenshot](assets/screenshot.jpg)

## Installation

### Prerequisites
- **Python 3.7**
- **Tkinter**: Tkinter is usually bundled with Python, but if not, you can install it via:
  ```bash
  sudo apt-get install python3-tk

- **requests:** Install it via:
  ```bash
    pip install requests
  ```
- **API Key** You'll need an API key from OpenWeather. Sign up for an account, create an API key, and replace the placeholder API_KEY in the code with your own.

## Setup
Clone this repository:

```bash
  git clone https://github.com/yourusername/WanderCast.git
```
Open the script and replace API_KEY with your actual OpenWeather API key.
Replace CITY with the desired location for the weather forecast.

- **Usage**
Run the program using:

```bash
python wandercast.py
```
- **Keyboard Controls**
  Esc: Exit fullscreen.
  F11: Toggle fullscreen.
  
- **Configuration**
Walker Speed: Modify WALKER_SPEED in milliseconds to control the animation speed.
Forecast Displayed Hours: Change for hour_data in data['list'][:4] to show a different number of forecast hours.

### Code Structure
```bash
random_color(): Generates a random color for the walker's animation.
```
```bash
get_weather_forecast(): Fetches and displays the weather forecast using the OpenWeather API.
```
```bash
update_datetime(): Updates the displayed date and time every second.
```
```bash
move_walker(): Controls the random walker animation within screen boundaries.
```

## Contributing
Feel free to fork this repository, submit issues, or make pull requests if you have ideas for enhancements.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

