"""docs"""

import tkinter as tk

BG_COLOR = "#ea6e28"
PARAGRAPH = "This is a sample paragraph for the typing speed application."
FONT_TEXT = ("Arial", 14)


class TypingSpeedApp:
    """docs"""

    def __init__(self, root: tk.Tk, paragraph: str) -> None:
        self.root = root
        self.root.title("Typing Spped Application")
        self.root.geometry("600x300")
        self.root.config(bg=BG_COLOR, padx=10, pady=10)
        # self.root.config(bg=BG_COLOR)

        self.paragraph = paragraph
        self.start_time = None
        self.end_time = None
        # Paragraph Label
        self.label_paragraph = tk.Label(
            root, text=self.paragraph, font=FONT_TEXT, wraplength=400
        )
        self.label_paragraph.pack(pady=20)
        # User Input Entry
        self.entry_input = tk.Entry(
            root,
            text="Enter the text here",
            bg="white",
            fg="blue",
            justify="center",
            width=50,
        )
        self.entry_input.pack(padx=20, pady=10)
        # Binding Keyboard Entry
        self.root.bind("<Key>", self.update_input)

    def update_input(self, event):
        """docs"""
        pass


window = tk.Tk()
app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
