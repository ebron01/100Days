from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

def search():
    searched_passwd = website_entry.get()
    try:
        with open("/home/beast/100Days/password_manager/passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Warning", message="There is no saved passwords at all!")
    else:
        try:
            passwd = data[searched_passwd]["password"]
            email = data[searched_passwd]["email"]
        except KeyError:
            messagebox.showerror(title="Warning", message=f"No saved password found for {searched_passwd}")
        else:
            messagebox.showinfo(title=f"{searched_passwd}", message=f"Email: {email} \n Password: {passwd}")
    finally:
        website_entry.delete(0,'end')
        website_entry.focus()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += ([choice(symbols) for char in range(randint(2, 4))])
    password_list += ([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()    
    email = email_entry.get() 
    password = password_entry.get() 
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }
    
    if len(website) == 0 or len(password)== 0 or len(email)== 0:
        messagebox.showerror(title="Warning", message="Details cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered \n {email}\n {password}\n Is it ok to save?")
    
        if is_ok:
            # with open("/home/beast/100Days/password_manager/passwords.txt", "a") as f:
            #     f.write(f"{website} | {email}  |  {password}  \n")
            try:
                with open("/home/beast/100Days/password_manager/passwords.json", "r") as f:
                    data = json.load(f)
                    
            except FileNotFoundError:
                with open("/home/beast/100Days/password_manager/passwords.json", "w") as f:
                    json.dump(new_data, f, indent=4)    
            else:
                data.update(new_data)
                with open("/home/beast/100Days/password_manager/passwords.json", "w") as f:
                    json.dump(data, f, indent=4) 
            finally:
                website_entry.delete(0,'end')
                email_entry.delete(0,'end')
                email_entry.insert(0, "eboran01@gmail.com")
                password_entry.delete(0,'end')
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="/home/beast/100Days/password_manager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1,sticky='e')

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky='e')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky='e')

#entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky='w', padx=10)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2, sticky='w', padx=10)
email_entry.insert(0, "eboran01@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w', padx=10)

#buttons
generator = Button(text="Generate Password", command=generate_password)
generator.grid(column=2, row=3, sticky='e')

adder = Button(text="Add", width=36, command=save)
adder.grid(column=1, columnspan=2, row=4)

searcher = Button(text="Search", command=search)
searcher.grid(column=2, row=1)

window.mainloop()