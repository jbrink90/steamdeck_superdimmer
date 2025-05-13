#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import subprocess
import base64
from io import BytesIO
from tkinter import PhotoImage

# Base64-encoded image
base64_image = """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"""

# Function to get the current brightness from xrandr
def get_current_brightness():
    try:
        # Get the output of xrandr command
        result = subprocess.check_output(["xrandr", "--verbose"])
        # Find the line containing brightness (adjust the string if needed)
        for line in result.decode().splitlines():
            if "Brightness" in line:
                # Return the current brightness value
                return float(line.split(":")[1].strip())
    except Exception as e:
        print(f"Error retrieving current brightness: {e}")
        return 1.0  # Default to 100% if there's an error

# Function to set the brightness using xrandr
def set_brightness(value):
    brightness = float(value)
    percent = int(brightness * 100)
    label_var.set(f"Brightness: {percent}%")

    # Execute the xrandr command to change brightness
    try:
        subprocess.run(["xrandr", "--output", "eDP", "--brightness", str(brightness)], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to set brightness:", e)

# Function to decrease brightness
def decrease_brightness():
    new_value = max(slider.get() - 0.10, 0.1)  # Ensure it doesn't go below 0.1
    slider.set(new_value)
    set_brightness(new_value)

# Function to increase brightness
def increase_brightness():
    new_value = min(slider.get() + 0.10, 1.0)  # Ensure it doesn't go above 1.0
    slider.set(new_value)
    set_brightness(new_value)

# Create the main window first
root = tk.Tk()
root.title("Steam Deck Brightness")
root.geometry("500x180")  # Set window size

# Decode the base64 string to binary data
image_data = base64.b64decode(base64_image)

# Convert binary data to a PhotoImage object after root window is created
icon_image = PhotoImage(data=image_data)

# Set the window icon (top-left corner)
root.iconphoto(True, icon_image)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to dock window at bottom-right corner
window_width = 500  # window width
window_height = 180  # window height
x_position = screen_width - window_width
y_position = screen_height - window_height

# Move the window to the bottom-right corner
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Label to show the current brightness
label_var = tk.StringVar()

# Get the current brightness from xrandr
current_brightness = get_current_brightness()

# Set the label text to reflect the brightness (as a percentage)
label_var.set(f"Brightness: {int(current_brightness * 100)}%")

# Set the slider to the current brightness
slider_value = current_brightness

# Label above the slider
label = tk.Label(root, textvariable=label_var, font=("Helvetica", 18), bg="white")
label.pack(pady=(20, 10))

# Frame to hold the buttons and slider
frame = tk.Frame(root, bg="white")
frame.pack(fill="x", padx=40, pady=10)

# Create the minus button
minus_button = tk.Button(frame, text="−", font=("Helvetica", 14), width=3, command=decrease_brightness)
minus_button.pack(side="left")

# Create the slider
slider = ttk.Scale(frame, from_=0.1, to=1.0, orient='horizontal', command=set_brightness)
slider.set(slider_value)  # Set slider to the current brightness value
slider.pack(side="left", fill='x', padx=10, expand=True, ipadx=10)

# Create the plus button
plus_button = tk.Button(frame, text="＋", font=("Helvetica", 14), width=3, command=increase_brightness)
plus_button.pack(side="right")

root.mainloop()
