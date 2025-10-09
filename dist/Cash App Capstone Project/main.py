from  tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

picked_word = {}
word_dic = {}

try:
    word_list = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dic = original_data.to_dict(orient="records")
else:

    word_dic = word_list.to_dict(orient="records")

timer = None

def flip_card():
    canvas.itemconfig(card_image,image=back_card_img)

    canvas.itemconfig(language_text,text="English")
    canvas.itemconfig(word_text,text= picked_word["English"])
    canvas.itemconfig(word_text,fill="white")
    canvas.itemconfig(language_text, fill="white")
    



def pick_word():
    global picked_word, timer 

    if timer is not None:
        window.after_cancel(timer)

    picked_word = random.choice(word_dic)

    canvas.itemconfig(language_text,text="French")
    canvas.itemconfig(word_text, text=picked_word["French"])
    canvas.itemconfig(card_image, image=front_card_img)
    canvas.itemconfig(word_text, fill="black")
    canvas.itemconfig(language_text, fill="black")
    timer = window.after(3000,flip_card)
def del_card():

    word_dic.remove(picked_word)
    print(len(word_dic))

    data = pandas.DataFrame(word_dic)
    data.to_csv("data/words_to_learn.csv",index=False)
    pick_word()

window = Tk()

window.title("Donno")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)


canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")

back_card_img = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400,263,image=front_card_img)
canvas.grid(row=0,column=0,columnspan=2)
language_text = canvas.create_text(400,150,text="Language",font=("Ariel", 40, "italic"),fill="black")
word_text = canvas.create_text(400,263,text="word",font=("Ariel", 60, "bold"),fill="black")

wrong_button_img = PhotoImage(file="images/wrong.png")
img= Button(window,image=wrong_button_img,command=pick_word)
img.grid(column=1,row=1)

right_button_img = PhotoImage(file="images/right.png")
img2= Button(window,image=right_button_img,command=del_card)
img2.grid(column=0,row=1)

pick_word()

window.mainloop()