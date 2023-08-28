from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()