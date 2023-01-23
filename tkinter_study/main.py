from tkinter import *


def click_button():
    number_mile = float(text.get())
    number.config(text=round(number_mile*1.609))


window = Tk()
window.title("Mile to Km Converter")
window.config(width=300, height=200, padx=30, pady=30)

text = Entry()
text.config(width=10)
text.grid(column=1, row=0)

mile = Label()
mile.config(text="Miles")
mile.grid(column=2, row=0)

is_equal_to = Label()
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)

number = Label()
number.config(text=0)
number.grid(column=1, row=1)

km = Label()
km.config(text="Km")
km.grid(column=2, row=1)

button = Button()
button.config(text="Calculate", command=click_button)
button.grid(column=1, row=2)






window.mainloop()
