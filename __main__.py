import tkinter as tk
from PIL import Image, ImageTk
import requests
import xml.etree.ElementTree as ET
import time
import slideshow
import clock
import scroller


def fetch_rss_feed(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Specify a user-agent to mimic a browser
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch RSS feed:", response.status_code)
        return None

def parse_rss_feed(xml_content):
    if xml_content:
        root = ET.fromstring(xml_content)
        items = root.findall('.//item')
        return items
    else:
        return None


def update_content(label):
    # Add a cache-busting parameter to the URL
    url = "https://www.cshub.com/rss/categories/attacks?" + str(int(time.time()))

    # Fetch the RSS feed
    xml_content = fetch_rss_feed(url)
    # Parse the XML content
    items = parse_rss_feed(xml_content)
    if items:
        # Extract titles of all entries
        all_entries = '\n'.join([item.find('title').text + '\n' for item in items])
        # Update the content on your display
        label.config(text=all_entries)
        print("Updating RSS..."+ url)
    else:
        label.config(text="Failed to fetch RSS feed")

    # Schedule the next update
    label.after(100000, update_content, label)  # Update every 10 seconds

def main():
    # Create the GUI
    root = tk.Tk()
    root.title("Digital Signage")
    root.configure(bg='black')
    root.attributes("-fullscreen", True)

    # Load the background image
    background_image = Image.open("bg.jpg")  # Change "bg.png" to your image file path
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the RSS feed content
    rss_frame = tk.Frame(root, bg="black")
    rss_frame.place(x=50, y=50)  # Adjust position as needed

    # Create a label to display content
    content_label = tk.Label(rss_frame, text="Content from RSS feed will appear here", wraplength=1400, font=('Arial', 12), fg='white', bg='black')
    content_label.pack(padx=10, pady=10, anchor='nw')

    # Specify path to image folder
    image_folder = 'images'
    slideshow_frame = slideshow.create_slideshow_frame(root, image_folder, interval=10)  # Display images every 3 seconds
    slideshow_frame.place(relx=0.675, rely=0.79, anchor='s')

    # Create a frame for the clock and date
    clock_and_date_frame = clock.create_clock_and_date_frame(root)
    clock_and_date_frame.place(relx=0.17, rely=0.9, anchor='s')  # Place in the middle of the GUI
    # Initial update
    update_content(content_label)

    scroller.main(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()