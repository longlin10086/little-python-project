BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
import pandas
import random


word_list = None

try:
    content = pandas.read_csv("./data/learned_word.csv")
except FileNotFoundError:
    content = pandas.read_csv("./data/ja_word.csv")
to_learn = content.to_dict(orient="records")


def translate():
    canvas.itemconfig(image, image=photo_back)
    canvas.itemconfig(title, text="Chinese", fill="white")
    canvas.itemconfig(word, text=word_list["chinese"], fill="white")


def next_card():
    global word_list, wait_word
    window.after_cancel(wait_word)
    canvas.itemconfig(image, image=photo_front)
    canvas.itemconfig(title, text="Japanese", fill="black")
    word_list = random.choice(to_learn)
    canvas.itemconfig(word, text=word_list["japanese"], fill="black")
    wait_word = window.after(3000, translate)


def is_known():
    global word_list
    to_learn.remove(word_list)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/learned_word.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="./images/card_front.png")
photo_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
image = canvas.create_image(400, 263, image=photo_front)


title = canvas.create_text(400, 130, text="Title", font=("Courier", 30, "italic"))
word = canvas.create_text(400, 270, text="word", font=("Courier", 45, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=2)

right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=2)

wait_word = window.after(3000, translate)
next_card()
























window.mainloop()

