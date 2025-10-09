from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")

    else:
        # if website in data:
        try:
            searched_email = data[website]["email"]
            searched_password = data[website]["password"]
            messagebox.showinfo(title=f"{website} login info",message= f"You email: {searched_email}\nYour password: {searched_password}")


        except KeyError:
            messagebox.showerror(title="Error", message="No info found for this Website")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "" or email == "" or len(password) < 8:

        messagebox.showwarning(title="Warning", message="Pls fill the Fields Correctly!")
    else:
       try:

            with open("data.json","r") as file:
                data = json.load(file)

       except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
       else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)
       finally:
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Donno")
window.config(pady=50,padx=50)
# window.tk.call('tk', 'scaling', 1.0)
# window.columnconfigure(0, weight=1)
# window.rowconfigure(0, weight=1)


canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)


#labels

website_text = Label(text="Website:")
website_text.grid(column=0,row=1)

email_text = Label(text="Email/username:")
email_text.grid(column=0,row=2)

pass_text = Label(text="Password:")
pass_text.grid(column=0,row=3)

#Entry

website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
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

search_button = Button(text="Search",command=search_password)
search_button.grid(column=2,row=1)


window.mainloop()


