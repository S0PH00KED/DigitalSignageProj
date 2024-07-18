import tkinter as tk
from PIL import Image, ImageTk
import os

def resize_image(image, target_size):
    """
    Resize the given image to the target size while maintaining aspect ratio.
    """
    width, height = image.size
    aspect_ratio = width / height
    new_width = int(target_size * 4 * aspect_ratio)
    new_height = int(target_size * 4)
    return image.resize((new_width, new_height))


def display_slideshow(image_folder, interval=1):
    """
    Display a slideshow of images from the specified folder with fade-in effect.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Slideshow")
    
    # Load and resize images
    images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.jpg', '.png'))]
    resized_images = [resize_image(Image.open(img), 200) for img in images]

    # Display images in a loop with fade-in effect
    photo_label = tk.Label(root)
    photo_label.pack()

    def show_image():
        idx %= len(resized_images)
        image = resized_images[idx]
        idx += 1
        root.after(interval * 3000, show_image)

    # Start the slideshow
    show_image()
    root.mainloop()

def create_slideshow_frame(parent, image, target_size=200):
    """
    Create a frame containing a slideshow of images from the specified folder with fade-in effect.
    """
    frame = tk.Frame(parent)
    frame.pack()

    # Load and resize images
    image = 'thistletv'
    resized_images = [resize_image(Image.open(image), target_size), image]

    # Display images in a loop with fade-in effect
    idx = 0
    photo_label = tk.Label(frame)
    photo_label.pack()

    def show_image():
        nonlocal idx
        idx %= len(resized_images)
        image = resized_images[idx]
        idx += 1
        frame.after(show_image)

    # Start the slideshow
    show_image()

    return frame
