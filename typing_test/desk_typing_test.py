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

var = {"word": "", "count": 0, "index": 0, "p_index": 0}
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

    def next_word_set(self):
        """docs"""
        var["word"] = ""
        var["index"] += 1
        var["count"] = 0

    def paragraph_and_word_index(self, increase: bool):
        """docs"""
        if increase:
            var["p_index"] += 1
            var["count"] += 1
        else:
            var["p_index"] -= 1
            var["count"] -= 1
        self.correct_negative_index()

    # t is a
    def change_letter_color(self, p_index, color, reset=False):
        """docs"""
        # Normal Cases
        list_index = var["index"]
        start = p_index
        end = p_index + 1
        # Space Conditions
        if reset and var["count"] != len(LST[list_index]):
            start = p_index - (len(LST[list_index]) + 1)
            end = p_index - 1
            tag_name = f"{self.paragraph[:p_index+1]}"
        elif reset:
            start = p_index - (len(LST[list_index]))
            end = p_index
            tag_name = f"{self.paragraph[:p_index+1]}"
        else:
            tag_name = (
                f"{list_index}.{LST[list_index]}.{p_index}.{self.paragraph[p_index]}"
            )

        self.text_paragraph.tag_add(tag_name, f"1.{start}", f"1.{end}")
        self.text_paragraph.tag_config(tag_name, foreground=color)

    def track_word_character(self, count, letter):
        """docs"""
        index = var["index"]
        paragraph_index = var["p_index"]
        word = LST[index]
        if count >= len(word) or paragraph_index >= len(self.paragraph):
            return
        if word[count] == letter:
            self.change_letter_color(p_index=paragraph_index, color="green")
        else:
            self.change_letter_color(p_index=paragraph_index, color="red")
        var["word"] += letter
        self.paragraph_and_word_index(increase=True)

    def word_space_compliance(self):
        """docs"""

    def correct_negative_index(self):
        """docs"""
        var["count"] = max(var["count"], 0)
        var["index"] = max(var["index"], 0)
        var["p_index"] = max(var["p_index"], 0)

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
                self.paragraph_and_word_index(increase=False)
                if len(var["word"]) > 1:
                    var["word"] = var["word"][:-1]
                else:
                    var["word"] = ""
                self.change_letter_color(p_index=var["p_index"], color="black")
            else:
                # if word count = 0 jump previous word in the LIST
                var["index"] -= 1
                # jumping previous word in the list means cursor
                # ont the previous word last letter
                var["count"] = len(LST[var["index"]])
                self.paragraph_and_word_index(increase=False)
                # deleted paragraph letter color is set black
                self.change_letter_color(p_index=var["p_index"], color="black")

        # Never let the any index (count) less than 0
        self.correct_negative_index()

        # if There is entry for word then pass next word
        if char == "space" and var["count"] > 0:
            if var["word"] == LST[var["index"]]:
                self.change_letter_color(
                    p_index=var["p_index"], color="gold2", reset=True
                )
                var["p_index"] += 1
            else:
                # Jumping next word beggining
                var["p_index"] += ((len(LST[var["index"]])) - var["count"]) + 1

                self.change_letter_color(
                    p_index=var["p_index"], color="red", reset=True
                )
            self.next_word_set()
            return

        if char not in all_keysyms:
            if stack:
                method = stack.pop()
                char = method(char)
            self.track_word_character(count=var["count"], letter=char)


# t is a

window = tk.Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
