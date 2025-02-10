from tkinter import *


def button_clicked():
    km = round(float(entry.get())*1.609, 2)
    km_calculated.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Arial", 12))
miles_text.grid(column=2, row=0)

equal_text = Label(text="is equal to", font=("Arial", 12))
equal_text.grid(column=0, row=1)

km_calculated = Label(text=0, font=("Arial", 12))
km_calculated.grid(column=1, row=1)

km_text = Label(text="Km", font=("Arial", 12))
km_text.grid(column=2, row=1)

button = Button(text="Calculate", font=("Arial", 10), command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
