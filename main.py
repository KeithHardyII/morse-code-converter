from tkinter import *
from tkinter import messagebox

"""
Morse Code Converter
Converts text to Morse code and Morse code back to text.
Built with Tkinter.
"""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# converts words into morse code separated by |
def convert_word():
    user_word = word_input.get()

    morse_code_list = []
    user_word = user_word.replace(" ", "")

    try:
        for letter in range(len(user_word)):
            morse_code_list.append((MORSE_CODE_DICT[user_word[letter].upper()]))
    except KeyError:
        messagebox.showerror(title="Error", message=f"Illegal character ({user_word[letter]}) in given word please try again.")
        return None

    morse_code_string = " | ".join(morse_code_list)
    converted_word_output.config(text=morse_code_string, font=(50))


# Converts morse code into words
def convert_code():
    string_list = []
    my_code = code_input.get().split()
    for x in range(len(my_code)):
        if my_code[x] in MORSE_CODE_DICT.values():
            # gets the dictionary key associated with the value my_code[x] and appends it the list string_list
            string_list.append(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(my_code[x])])
        else:
            messagebox.showerror(title="Error",
                                 message=f"This code does not exist ({my_code[x]}) please try again.")
            return None
    converted_code_output.config(text="".join(string_list), font=(50))


# Configures the Tkinter window
window = Tk()
window.title("Morse Code Converter")
window.config(padx=100, pady=100)
window.minsize(width=500, height=300)

word_instructions_label = Label(text="Please enter your word. Alphanumeric characters are accepted as well as: , . ? / - ( )")
word_instructions_label.grid(column=0, row=0,columnspan=3,pady=(0,20))

# Displays the ui for converting words to morse code
word_label = Label(text="Your Word:")
word_label.grid(column=0, row=1)
word_input = Entry(width=25)
word_input.grid(column=1, row=1)
word_input.focus()

converted_word_label = Label(text="Converted Word:", )
converted_word_label.grid(column=0, row=2)

converted_word_output = Label(text="N/A", font=(20))
converted_word_output.grid(column=1, row=2, columnspan=2)

word_to_code = Button(text="Convert", highlightthickness=0, command=convert_word, width=15)
word_to_code.grid(column=2, row=1)

# Displays the ui for converting morse code to words
code_label = Label(text="Your Code:")
code_label.grid(column=0, row=3)
code_input = Entry(width=25)
code_input.grid(column=1, row=3)

converted_code_label = Label(text="Converted Code:")
converted_code_label.grid(column=0, row=4)

converted_code_output = Label(text="N/A", font=(20))
converted_code_output.grid(column=1, row=4, columnspan=2)

code_to_word = Button(text="Convert", highlightthickness=0, command=convert_code, width=15)
code_to_word.grid(column=2, row=3)



# Keeps the window open while the program is running
window.mainloop()