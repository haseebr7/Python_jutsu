from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"
password = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if website == "" or password == "" or email == "" or len(password) < 8:

        messagebox.showwarning(title="Warning", message="Pls fill the Fields Correctly!")
    else:
        is_it = messagebox.askokcancel(title="Confirmation", message= f"So you wanna save \n{website} as website \n{email}as email\n{password} as password.\nRight naah?")

        if is_it:
            with open("data.txt", "a") as file:
                file.write(f"{website},{email},{password}\n")
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Donno")
window.config(pady=50,padx=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0,columnspan=3)


#labels

website_text = Label(text="Website:")
website_text.grid(column=0,row=1)

email_text = Label(text="Email/username:")
email_text.grid(column=0,row=2)

pass_text = Label(text="Password:")
pass_text.grid(column=0,row=3)

#Entry

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(END,"haseeburreyan@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1,row=3)
pass_entry.insert(0,string=password)

#button

pass_button = Button(text="Generate Password",command=pass_gen)
pass_button.grid(column=2,row=3)


add_button = Button(text="ADD",width=35,command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()


