"""Simple Type Testing APP"""

import string
import tkinter as tk
from all_keysyms import all_keysyms

letters = list(string.ascii_lowercase + string.ascii_uppercase + " ")
BG_COLOR = "#ea6e28"
ENTRY_DEFAULT_TEXT = "Enter the text here"
PARAGRAPH = (
    "This is a sample paragraph for the typing speed application " * 30
)

FONT_TEXT = ("Arial", 14)
TIMER = 60
var = {"word": "", "index": 0, "count": 0, "p_index": 0, "timer":TIMER}
stack = []
container = []


class TypingSpeedApp:
    """docs"""

    def __init__(self, root: tk.Tk, paragraph: str) -> None:
        self.list = PARAGRAPH.split()
        self.root = root
        self.root.title("Typing Speed Application")
        self.root.geometry("600x400")
        self.root.config(bg=BG_COLOR, padx=10, pady=5)

        self.paragraph = " ".join(self.list)
        self.start_time = None
        self.end_time = None
        self.char = None


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
        self.text_paragraph.grid(row=0, column=0, sticky="n", pady=10)
        # User Input Entry
        self.entry_input = tk.Entry(
            root,
            bg="white",
            fg="blue",
            justify="center",
            width=30,
            font=FONT_TEXT,
            bd=8
        )
        self.entry_input.grid(row=3, column=0, sticky="n", pady=10 )
        self.entry_input.insert(0, ENTRY_DEFAULT_TEXT)
        self.entry_input.bind("<FocusIn>", self.on_entry_click)

        # Binding Keyboard Entry
        self.entry_input.bind("<KeyRelease>", self.update_input)

        # LABEL TIMER
        self.label_timer = tk.Label(self.root,text="Timer",
                               font=("cooper black", 28,"bold italic"), bg=BG_COLOR, fg="red")
        # LABEL TIME
        self.label_time = tk.Label(self.root,text="60",
                              font=("Castellar", 28,"bold italic"), bg=BG_COLOR)
        # BUTTONS
        self.button_try_again = tk.Button(self.root, text="Try Again", command=self.restart)


    def run_timer(self):
        """docs"""
        self.label_timer.grid(row=1, column=0)
        self.label_time.grid(row=2, column=0)
        self.label_time.config(text=f"{var['timer']}")
        var["timer"] -= 1
        if var["timer"] <= 0:
            var["timer"] = 3
            self.show_result()
            self.entry_input.config(state=tk.DISABLED)
        else:
            self.label_time.after(1000, self.run_timer)

    def show_result(self):
        """docs"""
        self.label_timer.destroy()
        self.label_time.destroy()
        gross, net = self.calculate_wpm()
        self.text_paragraph.grid(row=0,column=0, columnspan=2,sticky="ew")
        label_gross = tk.Label(text=f"Gross WPM: {gross}", font=FONT_TEXT, bg=BG_COLOR)
        label_gross.grid(row=1,column=0, sticky="w")
        label_net = tk.Label(text=f"Net WPM: {net}", font=FONT_TEXT, bg=BG_COLOR)
        label_net.grid(row=1, column=1, sticky="w")
        self.button_try_again.grid(row=2, column=0)

    def restart(self):
        """docs"""
        self.root.destroy()
        new_window = tk.Tk()
        new_app = TypingSpeedApp(new_window, PARAGRAPH)
        new_app.root.mainloop()



    def calculate_wpm(self):
        """docs"""
        true_counts = container.count(True)
        false_counts = container.count(False)
        gross_wpm = ((true_counts + false_counts)/5) / (TIMER // 60)
        net_wpm = gross_wpm - ((false_counts)/5) / (TIMER // 60)
        return gross_wpm, net_wpm

    def on_entry_click(self, _):
        """docs"""
        self.entry_input.delete(0, tk.END)
        self.entry_input.config(fg="black")
        self.run_timer()

    def next_word_set(self):
        """docs"""
        var["word"] = ""
        var["index"] += 1
        var["count"] = 0

    def paragraph_and_word_index(self, ascent: bool):
        """docs"""
        if ascent:
            var["p_index"] += 1
            var["count"] += 1
        else:
            var["p_index"] -= 1
            var["count"] -= 1
            self.correct_negative_index()



    def change_letter_color(self, p_index, color, reset=False):
        """docs"""

        word = self.list[var["index"]]
        current_text = self.text_paragraph.get("1.0", tk.END)
        tag_name = f"{self.list[var["index"]]}[{var['index']}:{var['count']}]"
        if reset:
            start = p_index - (len(word))
            end = start + len(word)
        else:
            start = p_index
            end = p_index + 1

        # Save current text in TEXT
        first_part = current_text[start:end]
        second_part = current_text[end:]

        # Delete current text content
        self.text_paragraph.delete(f"1.{start}", tk.END)
        # Add slice of text in order
        self.text_paragraph.insert(tk.END, first_part)
        self.text_paragraph.insert(tk.END, second_part)

        self.text_paragraph.tag_add(tag_name, f"1.{start}", f"1.{end}")
        self.text_paragraph.tag_config(tag_name, foreground=color, background="gold2")

    def track_word_character(self, count, letter):
        """docs"""
        index = var["index"]
        paragraph_index = var["p_index"]
        word = self.list[index]
        if count >= len(word) or paragraph_index >= len(self.paragraph):
            return
        if word[count] == letter:
            self.change_letter_color(p_index=paragraph_index, color="green")
        else:
            self.change_letter_color(p_index=paragraph_index, color="red")
        var["word"] += letter
        self.paragraph_and_word_index(ascent=True)

    def correct_negative_index(self):
        """docs"""
        var["count"] = max(var["count"], 0)
        var["index"] = max(var["index"], 0)
        var["p_index"] = max(var["p_index"], 0)

    def back_space_actions(self):
        """doc"""
        # BackSpace, where text is active in entry box
        # if self.entry_input.get():
        if var["count"] > 0 and self.char != "space":
            self.paragraph_and_word_index(ascent=False)
            if len(var["word"]) > 1:
                var["word"] = var["word"][:-1]
            else:
                var["word"] = ""
            self.change_letter_color(p_index=var["p_index"], color="black")
        # BackSpace, text does not exist in entry box
        else:
            # if word count = 0 jump previous word in the LIST
            var["index"] -= 1
            var["index"] = max(var["index"],0)
            if self.list[var["index"]]:
                var["count"] = len(self.list[var["index"]]) - 1
            var["p_index"] -= 2
            var["p_index"] = max(var["p_index"], 0)
            if self.paragraph[var["p_index"]] != " ":
                self.change_letter_color(p_index=var["p_index"], color="black")
            if container:
                container.pop()
    def space_actions(self, char):
        """docs"""
        # Ignore, none entered char + space
        if char == "space" and var["count"] > 0:
            # the entered word is the same as the word in the list + space
            if var["word"] == self.list[var["index"]]:
                self.change_letter_color(
                    p_index=var["p_index"], color="green", reset=True
                )
                var["p_index"] += 1
                container.append(True)
            # the entered word length less than the word in the list + space
            elif len(var["word"]) < len(self.list[var["index"]]):
                # new_index = current_index - (length of word - entered word count) + 1
                var["p_index"] += ((len(self.list[var["index"]])) - var["count"]) + 1

                self.change_letter_color(
                    p_index=var["p_index"], color="red", reset=True)
                container.append(False)
            # the entered word length more than the word in the list + space
            elif len(var["word"]) > len(self.list[var["index"]]):
                # new_index = current_index - entered_total_word # returns beginning of the word
                # new_index += length of word # goes to next space of the end of the word
                var["p_index"] = (var["p_index"] - len(var["word"])) +  len(self.list[var["index"]])

                self.change_letter_color(
                    p_index=var["p_index"], color="red", reset=True)
                container.append(False)
            else:
                # word not equal, go to next char of paragraph
                var["p_index"] += 1
                container.append(False)
            self.entry_input.delete(0, tk.END)
            self.next_word_set()

    def print_report(self,):
        """doc"""
        print("Current Word: ",self.list[var["index"]])
        print(f"Current Char: {self.paragraph[var['index']]}")


    def update_input(self, event):
        """docs"""
        # Ignore to keep holding non-alphabetic keys entry
        # and deteck capitilaze of letter request
        # Pressing Shift, trigger the event 2 times

        self.char = event.keysym
        if self.char == "Return":
            self.print_report()
        if self.char in ("Shift_L", "Shift_R") and len(stack) == 0:
            stack.append(str.upper)
        # Delete letter while there are letter left
        if self.char == "BackSpace":
            self.back_space_actions()
        # Never let the any index (count) less than 0
        self.correct_negative_index()

        # if There is entry for word then pass next word
        self.space_actions(char=self.char)
        if self.char not in all_keysyms:
            if stack:
                method = stack.pop()
                self.char = method(self.char)
            self.track_word_character(count=var["count"], letter=self.char)
        print(container)





window = tk.Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

app = TypingSpeedApp(root=window, paragraph=PARAGRAPH)
window.mainloop()
