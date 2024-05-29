## General

Building GUI applications with Python, desktop app that assesses typing speed. Give the user some sample text and detect how many words they can type per minute.

### Mechanism

It converts the given paragraph into a list with the split method and checks the letter order of the words in the list with <code>var["count"]</code>. A third index, p_index, is used for indexical operations on paragraphs.
Its value is determined by keyboard input.

## LOGIC

### Paragraph Index

**Text Widget** inserted text index is initiated in global <code>var["p_index"]</code> on every entry, backSpace and space event call, runs its appropriate method to increase or decrase index (for tracking list), count (length of the word in list index), p_index (Text widget inserted text index)

### Space Logic

- Prevents space assignments without entering any letters.
- The space key pressed while entering a letter resets the relevant key values ​​in the var variable for the new word in the list. If the letters entered from the keyboard do not match the word in the list, the color assignment (green, red) is gets controlled in the <code>space_actions</code> method.
  <br><br>
- p_index jumps on the next word 0 index every valid space KeyRelease

### Backspace Logic

**BackSpace** Where text in the Entry Box <br>
Entry widget Click event disturbs the debugging, Disable it to run debugger

<ul>
<li>While word count not 0, it uses real `p_index`</li>
</ul>

**BackSpace** Entry Box is empty

<ul>
    <li>Get previous word and Set <code>p_index to end of the word index</code>
        <ul>
            <li>To DO that reduce current list <code>index -= 1</code></li>
            <li>Previous word <code>self.list[var["count"]]</code>So; <br>count = len(word) - 1</code></li>
            <li>To get the previous word last character <code>p_index -= 2</code></li>
        </ul>
    </li>
</ul>
