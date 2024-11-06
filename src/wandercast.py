import tkinter as tk
import random
import time
from weather_forecast import Weather

# Animation settings
WALKER_SPEED = 50
WALKER_RADIUS = 5
TRACK_RADIUS = 2
MAX_STEPS = 1000


# Function to generate a random color
def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"


# Fullscreen toggle functions
def toggle_fullscreen():
    root.attributes('-fullscreen', True)
    root.bind('<Escape>', end_fullscreen)


def end_fullscreen():
    root.attributes('-fullscreen', False)
    root.bind('<F11>', toggle_fullscreen)


# Initialize main window
root = tk.Tk()
root.title("Wandercast")
root.bind('<Escape>', end_fullscreen)

# Set canvas dimensions
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()

# Create a single canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


#INITIALZING
W = Weather(canvas, "Stockholm")


# Initial walker position and step count
x, y = WIDTH // 2, HEIGHT - HEIGHT // 4
step_count = 0

# Create text elements to display time, date, and weather
time_text = canvas.create_text(WIDTH // 2, HEIGHT // 4, text="", font=("Helvetica", 150, "bold"), fill="black")
date_text = canvas.create_text(WIDTH // 2, HEIGHT // 4 + 90, text="", font=("Helvetica", 40), fill="black")


# Function to reset the walker
def reset_walker_canvas():
    global x, y, step_count
    canvas.delete("walker")
    x, y = WIDTH // 2, HEIGHT - HEIGHT // 4
    step_count = 0


# Function to update the current date and time display
def update_datetime():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y-%m-%d")

    canvas.itemconfig(time_text, text=current_time)
    canvas.itemconfig(date_text, text=current_date)
    root.after(1000, update_datetime)


# Function to move the walker
def move_walker():
    global x, y, step_count
    step_count += 1

    if step_count >= MAX_STEPS:
        reset_walker_canvas()

    # Check for collision with tracks by finding overlapping items
    overlap = canvas.find_overlapping(x - WALKER_RADIUS, y - WALKER_RADIUS, x + WALKER_RADIUS, y + WALKER_RADIUS)
    color = random_color() if len(overlap) > 1 else "blue"

    # Draw track and walker
    canvas.create_oval(
        x - TRACK_RADIUS, y - TRACK_RADIUS, x + TRACK_RADIUS, y + TRACK_RADIUS,
        fill="blue", outline="blue", tags="walker"
    )
    canvas.create_oval(
        x - WALKER_RADIUS, y - WALKER_RADIUS, x + WALKER_RADIUS, y + WALKER_RADIUS,
        fill=color, outline=color, tags="walker"
    )

    # Choose a random direction (up, down, left, right)
    dx, dy = random.choice([(0, -10), (0, 10), (-10, 0), (10, 0)])

    # Update position with boundary checks
    x = max(WALKER_RADIUS, min(x + dx, WIDTH - WALKER_RADIUS))
    y = max(HEIGHT // 2 + 100, min(y + dy, HEIGHT - WALKER_RADIUS))

    # Call this function again after a short delay
    root.after(WALKER_SPEED, move_walker)


# Start functions and Tkinter main loop
move_walker()
update_datetime()
W.get_forecast()
root.mainloop()
