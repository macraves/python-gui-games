"""Simple Type Testing APP"""

import string
import tkinter as tk
from all_keysyms import all_keysyms

letters = list(string.ascii_lowercase + string.ascii_uppercase + " ")
BG_COLOR = "#ea6e28"
ENTRY_DEFAULT_TEXT = "Enter the text here"
PARAGRAPH = "This is a sample paragraph for the typing speed application."
FONT_TEXT = ("Arial", 14)


class TypingSpeedApp:
    """docs"""

    def __init__(self, root: tk.Tk, paragraph: str) -> None:
        self.root = root
        self.root.title("Typing Speed Application")
        self.root.geometry("600x300")
        self.root.config(bg=BG_COLOR, padx=10, pady=10)

        self.paragraph = paragraph
        self.start_time = None
        self.end_time = None

        # Paragraph Label
        self.label_paragraph = tk.Label(
            root, text=self.paragraph, font=FONT_TEXT, wraplength=400, bg="white"
        )
        self.label_paragraph.grid(row=0, column=0, sticky="n", pady=20)

        # User Input Entry
        self.entry_input = tk.Entry(
            root,
            bg="white",
            fg="blue",
            justify="center",
            width=30,
            font=FONT_TEXT,
        )
        self.entry_input.grid(row=1, column=0, sticky="n", pady=10)
        self.entry_input.insert(0, ENTRY_DEFAULT_TEXT)
        self.entry_input.bind("<FocusIn>", self.on_entry_click)

        # Binding Keyboard Entry
        self.entry_input.bind("<KeyRelease>", self.update_input)

    def on_entry_click(self, event):
        """docs"""
        if self.entry_input.get() == ENTRY_DEFAULT_TEXT:
            self.entry_input.delete(0, tk.END)
            self.entry_input.config(fg="black")

    def update_input(self, event):
        """docs"""
        char = event.keysym
        if char not in all_keysyms:
            letter = self.entry_input.get()
            print(letter)


window = tk.Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
