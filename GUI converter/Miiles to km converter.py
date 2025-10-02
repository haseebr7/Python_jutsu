from tkinter import *

window = Tk()
window.title("Random")
window.config(padx=20,pady=20)


def mile_to_km():
    miles = float(miles_input.get())
    km =  miles * 1.689
    converted.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

my_label = Label(text = "Miles")
my_label.grid(column=2,row=0)

convert = Label(text = "is = to")
convert.grid(column=0,row=1)


converted = Label(text="0")
converted.grid(column=1,row=1)

converted_uiop = Label(text="KM")
converted_uiop.grid(column=2,row=1)


button_to_convert = Button(text="Calculate",command=mile_to_km)
button_to_convert.grid(column=2,row=2)


window.mainloop()