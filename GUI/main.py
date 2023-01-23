from tkinter import *

#button func
def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #adds padding to all components created in this window

#label
my_label = Label(text="This is the text for label", font=("Arial", 24, "italic"))
my_label.config(text="this is newly updated text")
# my_label.pack()
# my_label.place(x=100, y=50)
my_label.grid(column=1, row=1)

#button
button = Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(column=2, row=2)

#entry
input = Entry()
input.config(width=10)
# input.pack()
input.grid(column=3, row=3)


#one of the pack or  grid must be used.
#place can be used with others  







window.mainloop()