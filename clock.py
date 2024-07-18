import tkinter as tk
import time

def update_clock(label):
    current_time = time.strftime('%I:%M:%S %p')  # Format the current time
    label.config(text=current_time)
    label.after(1000, update_clock, label)  # Update every 1 second

def create_clock_and_date_frame(parent):
    frame = tk.Frame(parent, bg='black')  # Set background color
    frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Add border
    frame.pack(pady=20)  # Add padding

    # Create a label for the clock
    clock_label = tk.Label(frame, font=('Verdana', 50), fg='white', bg='black')  # Change font to Helvetica
    clock_label.pack()

    # Create a label for the date
    date_label = tk.Label(frame, font=('Arial', 20), fg='white', bg='black')  # Customize font and color
    date_label.pack()

    # Update the clock
    update_clock(clock_label)

    # Update the date
    current_date = time.strftime('%A, %B %d, %Y')  # Format the current date
    date_label.config(text=current_date)

    return frame