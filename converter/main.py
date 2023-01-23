from tkinter import *

def calculate():
    num_miles = miles_input.get()
    num_km = float(num_miles) * 1.60934 
    label_km.config(text=num_km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20, background="white", highlightbackground=None)

#label1
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#label2
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#label3
km = Label(text="Km")
km.grid(column=2, row=1)

#label_km
label_km = Label(text="0")
label_km.grid(column=1, row=1)

#Entry
miles_input = Entry()
miles_input.config(width=7)
miles_input.grid(column=1, row=0)

#button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


    











window.mainloop()