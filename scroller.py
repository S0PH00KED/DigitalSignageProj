import requests
import xml.etree.ElementTree as ET
import tkinter as tk
import time

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

def update_news_scroll(text_widget):
    # URL of the RSS feed
    rss_url = "https://www.cisa.gov/cybersecurity-advisories/cybersecurity-advisories.xml"
    
    # Fetch the RSS feed
    xml_content = fetch_rss_feed(rss_url)
    # Parse the XML content
    items = parse_rss_feed(xml_content)
    if items:
        # Extract titles of all entries
        all_entries = '... '.join([item.find('title').text for item in items])  # Join titles with separator
        # Update the content on your display
        text_widget.delete('1.0', tk.END)  # Clear existing content
        text_widget.insert(tk.END, all_entries)
        print("Updating news scroll..."+ rss_url)
    else:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Failed to fetch news scroll content")

def scroll_news(text_widget):
    # Scroll the text widget horizontally
    text_widget.xview_scroll(1, 'units')  # Scroll 1 unit to the right
    # Check if scrolled to the end
    if text_widget.xview()[1] == 1.0:
        # Reset scroll position to the beginning
        text_widget.xview_moveto(0)
    # Schedule the next scroll after a short delay
    text_widget.after(100, scroll_news, text_widget)  # Adjust the delay as needed

def main(parent):
    # Create a frame for the news scroller
    news_frame = tk.Frame(parent, bg="black", border=1)
    news_frame.place(x=100, y=1000, relwidth=0.9, relheight=0.04)  # Adjust position and size as needed

    # Create a text widget for displaying the news scroll
    news_text = tk.Text(news_frame, bg="black", fg="yellow", font=("Arial", 20), wrap="none")  # Set wrap to "none"
    news_text.pack(side="left", fill="both", expand=True)

    # Start updating the news scroll
    update_news_scroll(news_text)
    
    # Start scrolling the news horizontally
    scroll_news(news_text)

if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()
