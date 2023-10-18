BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
WORD_DISPLAYED = {}
words = {}

def flip_card():
    current_word_english = WORD_DISPLAYED["English"]
    canva.itemconfig(main_canva, image=back)
    canva.itemconfig(title, text="English", fill="white")
    canva.itemconfig(canva_word, text=current_word_english, fill="white")


window = Tk()
window.title("Flashy")
window.config(bg= BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
right_photo = PhotoImage(file="./images/right.png")
wrong_photo = PhotoImage(file="./images/wrong.png")
canva = Canvas(width=800, height=526)
main_canva = canva.create_image(400, 263, image=front)
canva.grid(row=0, column=0, columnspan=2)
canva.config(borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
title = canva.create_text(400, 150, text="", font=("Ariel", 60, "italic"))
canva_word = canva.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


try:
    french_words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    words = french_words.to_dict(orient="records")
else:
    words = french_words.to_dict(orient="records")


def button_click():
    global WORD_DISPLAYED, flip_timer
    window.after_cancel(flip_timer)
    WORD_DISPLAYED = random.choice(words)
    canva.itemconfig(main_canva, image=front)
    current_word_french = WORD_DISPLAYED["French"]
    canva.itemconfig(title, text="French", fill="black")
    canva.itemconfig(canva_word, text=current_word_french, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    words.remove(WORD_DISPLAYED)
    print(len(words))
    new_data = pandas.DataFrame(words)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    button_click()


right_button = Button(image=right_photo, highlightthickness=0,borderwidth=0, command=is_known)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_photo, highlightthickness=0, borderwidth=0, command=button_click)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

button_click()

window.mainloop()
