"""Graphical User Interface for watermarking images.

This module provides a graphical user interface (GUI) for adding watermarks to images.
It uses the tkinter library for creating the GUI and the PIL library for image processing.

The main features of this GUI include:
- Opening an image file
- Displaying the selected image
- Adding a watermark to the image

To use this GUI, run the script and click on the "Open Image" button to select an image file.
The selected image will be displayed in the GUI. Then, click on the "Add Watermark" button to
select a watermark image file and add the watermark to the main image.

Note: This GUI requires the watermark_funcs module to be imported, which provides the necessary
functions for adding watermarks to images.

Example:
    $ python main_gui.py
"""

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from watermark_funcs import Image, paste_watermark

LABEL_WIDTH = 100
LABEL_HEIGHT = 20

BACKGROUND_COLOR = "#B1DDC6"
image_files = {}


def set_image_label(file_path):
    """Set the image label with the selected image.

    Args:
        file_path (str): The path to the selected image file.
    """
    if file_path:
        img = Image.open(file_path)
        width, height = img.size
        # Change Label Size
        label_image.config(width=width, height=height)
        # Convert the Image PhotoImage format
        img_tk = ImageTk.PhotoImage(img)
        # Display Image
        label_image.config(image=img_tk)
        label_image.image = img_tk
        image_files["main_image"] = file_path


def image_label():
    """Open an image file and set the image label."""
    file_path = open_image()
    set_image_label(file_path=file_path)


def open_image():
    """Opens a file dialog to select an image file.

    Returns:
        str: The path to the selected image file.
    """
    file_path = filedialog.askopenfilename()
    return file_path


def add_watermark():
    """Open a watermark image file and add the watermark to the main image."""
    file_path = open_image()
    if file_path:
        main_path = image_files.get("main_image")
        new_file_path = paste_watermark(main_path=main_path, watermark_path=file_path)
        set_image_label(file_path=new_file_path)


window = tk.Tk()
window.title("Watermarking")
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)

# canvas_photo = tk.Canvas(width=600, height=400, highlightthickness=0)
# canvas_photo.grid(row=0, column=0, columnspan=3)
label_image = tk.Label(window, width=LABEL_WIDTH, height=LABEL_HEIGHT)
label_image.grid(row=0, column=0, columnspan=3)

button_open = tk.Button(window, text="Open Image", command=image_label)
button_open.grid(row=1, column=0, sticky="W", pady=10)

button_image_watermark = tk.Button(window, text="Add Watermark", command=add_watermark)
button_image_watermark.grid(row=1, column=1, sticky="W")


window.mainloop()
