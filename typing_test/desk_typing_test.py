"""Simple Type Testing APP"""

import string
import tkinter as tk
from all_keysyms import all_keysyms

letters = list(string.ascii_lowercase + string.ascii_uppercase + " ")
BG_COLOR = "#ea6e28"
ENTRY_DEFAULT_TEXT = "Enter the text here"
PARAGRAPH = (
    "t is a sample paragraph for the typing speed application "
    "This is a sample paragraph for the typing speed application "
)
LST = PARAGRAPH.split()
FONT_TEXT = ("Arial", 14)

var = {"count": 0, "index": 0, "word": "", "next": False}
container = []
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

    def get_paragraph_index(self, index, count):
        """doc"""
        length = 0
        if index != 0:
            for i in range(index):
                length += len(LST[i]) + 1
        else:
            length = count
        return length, self.paragraph[length]

    def change_leter_color(self, index, count, color):
        """docs"""
        length, _ = self.get_paragraph_index(index, count)

        tag_name = f"{index}.{LST[index]}.{LST[index]}{count}"
        self.text_paragraph.tag_add(
            tag_name, f"1.{length+count}", f"1.{length+count+1}"
        )
        self.text_paragraph.tag_config(tag_name, foreground=color)

    def next_word_set(self):
        """docs"""
        var["word"] = ""
        var["index"] += 1
        var["count"] = 0

    def print_details(self, index, count):
        """docs"""
        print(
            f"{self.get_paragraph_index(index, count)[0]}. index "
            f"{self.get_paragraph_index(index, count)[1]}"
        )

    def track_word_character(self, count, letter):
        """docs"""
        index = var["index"]
        self.print_details(index, count)
        word = LST[index]
        if count < len(word):
            if letter == word[count]:
                self.change_leter_color(index=index, count=count, color="green")
            else:
                print(letter + " wrong entry")
                self.change_leter_color(index=index, count=count, color="red")
            var["word"] += letter
            var["count"] += 1
        if var["word"] == word:
            container.append(var["word"])
            self.next_word_set()
            var["next"] = True
        if len(var["word"]) == len(word):
            self.next_word_set()

    def update_input(self, event):
        """docs"""
        # Ignore to keep holding non-alphabetic keys entry
        # and deteck capitilaze of letter request
        # Pressing Shift, trigger the event 2 times
        char = event.keysym
        if char in ("Shift_L", "Shift_R") and len(stack) == 0:
            stack.append(str.upper)
        # Delete letter while there are letter left
        if char == "BackSpace":
            if var["count"] > 0:
                var["count"] -= 1
                var["word"] = var["word"][:-1]

                self.change_leter_color(
                    index=var["index"], count=var["count"], color="black"
                )

            else:
                var["index"] -= 1
                var["index"] = max(var["index"], 0)
                var["count"] = len(LST[var["index"]])
                self.change_leter_color(
                    index=var["index"], count=var["count"], color="black"
                )
        # Never let the word index (count) less than 0
        var["count"] = max(var["count"], 0)

        # in a case any letter entered, enable space
        if char == "space" and var["count"] > 0:
            self.next_word_set()

        if char not in all_keysyms:
            if stack:
                method = stack.pop()
                char = method(char)
            self.track_word_character(count=var["count"], letter=char)


window = tk.Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
