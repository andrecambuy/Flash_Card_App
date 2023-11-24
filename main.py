from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"



data = read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')



def get_random_word():

    current_card = random.choice(data_dict)
    current_card['English']
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text=current_card['French'])


# UI setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")


right_button = Button(image=right_image, highlightthickness=0, command=get_random_word)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=0, row=1)



get_random_word()


window.mainloop()