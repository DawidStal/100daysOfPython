from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
# Reading data
try:
    data = pandas.read_csv("Day-30-Flash-Cards\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Day-30-Flash-Cards\\data\\french_words.csv")
words = data.to_dict("records")
print(words)


# Functions
def remove_word():  
    words.remove(current_word)
    words_to_learn = pandas.DataFrame(data=words)
    words_to_learn.to_csv("Day-30-Flash-Cards\\data\\words_to_learn.csv", index=False)
    new_word()


def new_word():
    global current_word, flip_timer
    current_word = random.choice(words)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=front_card_image)
    canvas.itemconfig(language, fill="black", text="French")
    canvas.itemconfig(word, fill="black", text=current_word["French"])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(language, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=current_word["English"])


# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_card_image = PhotoImage(file="Day-30-Flash-Cards\\images\\card_front.png")
back_card_image = PhotoImage(file="Day-30-Flash-Cards\\images\\card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 263, image=front_card_image)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="Day-30-Flash-Cards\\images\\wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="Day-30-Flash-Cards\\images\\right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

canvas.itemconfig(language, text="French")
new_word()

window.mainloop()
