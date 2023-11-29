from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}


try:
    data = read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')



def get_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,  text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_know():
    data_dict.remove(current_card)
    print(len(data_dict))
    data = DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    

    get_random_word()




# UI setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")


right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=0, row=1)



get_random_word()


window.mainloop()