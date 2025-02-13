import tkinter as tk
import pyautogui
import threading
import time

# Function to simulate mouse click after delay
def click_after_delay():
    delay = int(delay_entry.get())  # Get the delay time in seconds
    time.sleep(delay)  # Wait for the specified time
    pyautogui.click()  # Perform the click

    result_label.config(text=f"Clicked after {delay} seconds!")

# Function to handle the button click event
def start_click():
    # Start the click process in a new thread
    click_thread = threading.Thread(target=click_after_delay)
    click_thread.start()

# Set up the UI
root = tk.Tk()
root.title("Auto Clicker")

# Create a label for instructions
label = tk.Label(root, text="Enter the time delay in seconds:")
label.pack(pady=10)

# Create an entry widget for the delay time
delay_entry = tk.Entry(root)
delay_entry.pack(pady=10)

# Create a button to start the click process
start_button = tk.Button(root, text="Start Clicking", command=start_click)
start_button.pack(pady=20)

# Create a label to show the result after clicking
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the UI
root.mainloop()
