"""Simple Type Testing APP"""

import string
import tkinter as tk
from all_keysyms import all_keysyms

letters = list(string.ascii_lowercase + string.ascii_uppercase + " ")
BG_COLOR = "#ea6e28"
ENTRY_DEFAULT_TEXT = "Enter the text here"
PARAGRAPH = (
    "This is a sample paragraph for the typing speed application "
    "This is a sample paragraph for the typing speed application "
)
LST = PARAGRAPH.split()
FONT_TEXT = ("Arial", 14)
counters = {"count": 0, "index": 0}
stack = []


class TypingSpeedApp:
    """docs"""

    def __init__(self, root: tk.Tk, paragraph: str) -> None:
        self.root = root
        self.root.title("Typing Speed Application")
        self.root.geometry("600x300")
        self.root.config(bg=BG_COLOR, padx=10, pady=10)

        self.paragraph = " ".join(LST)
        self.start_time = None
        self.end_time = None

        # # Paragraph Label
        # self.label_paragraph = tk.Label(
        #     root, text=self.paragraph, font=FONT_TEXT, wraplength=400, bg="white"
        # )
        # self.label_paragraph.grid(row=0, column=0, sticky="n", pady=20)

        # Text Widget
        self.text_paragraph = tk.Text(
            root,
            font=("Arial", 14),
            wrap="word",
            bg="white",
            height=5,
            width=50,
        )
        self.text_paragraph.insert(tk.END, paragraph)
        self.text_paragraph.config(state="disabled")
        self.text_paragraph.grid(row=0, column=0, sticky="n", pady=20)

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
        # self.entry_input.insert(0, ENTRY_DEFAULT_TEXT)
        # self.entry_input.bind("<FocusIn>", self.on_entry_click)

        # Binding Keyboard Entry
        self.entry_input.bind("<KeyRelease>", self.update_input)

    # def on_entry_click(self, event):
    #     """docs"""
    #     if self.entry_input.get() == ENTRY_DEFAULT_TEXT:
    #         self.entry_input.delete(0, tk.END)
    #         self.entry_input.config(fg="black")

    def change_leter_color(self, word: str, is_true: bool, reset=False):
        """docs"""

    def track_word_character(self, count, letter):
        """docs"""
        index = counters["index"]
        word = LST[index]
        if letter == word[count]:
            pass

    def update_input(self, event):
        """docs"""

        count = counters["count"]
        char = event.keysym
        if char in ("Shift_L", "Shift_R") and len(stack) == 0:
            stack.append(str.upper)
        if char == "BackSpace":
            counters["count"] -= 1
            counters["count"] = max(counters["count"], 0)
        if char not in all_keysyms:
            if stack:
                method = stack.pop()
                char = method(char)
            self.track_word_character(count=count, letter=char)
            print(char)
            counters["count"] += 1


window = tk.Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
