from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import csv

FONT = ("arial", 15, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ✔TODO: create lists with alphabet, symbols and numbers
# ✔TODO: random pick 2 numbers, 1 symbol and 7 letters and shuffle before execution
# TODO: later improve to popup new window and ask for parameter how many characters
# of which how many letters, symbols, numbers should be

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']
symbols = [".", ",", "*", "@", "!", ">", "<", "=", "+", "-", "^", "#",
           "&", "[", "]", "(", ")", "$", "%", "?"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def pwd_gen():
    # remove any written chracters
    entry_pwd.delete(first=0, last=END)
    # create random string with set amount of characters
    l_letters = [choice(alphabet) for l in range(randint(5, 8))]
    l_numbers = [choice(numbers) for n in range(randint(2, 3))]
    l_symbols = [choice(symbols) for s in range(randint(1, 2))]

    pass_list = l_letters + l_numbers + l_symbols
    shuffle(pass_list)
    gen_pwd = "".join(pass_list)

    # insert generated password into entry window
    entry_pwd.insert(END, gen_pwd)
    # also add generated password into clipboard(copy)
    entry_pwd.clipboard_append(gen_pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# ✔TODO: save entries into csv file
# TODO: check possibility to work with pass protected csv file and how to manage
# TODO: set minumum lenght of password
def pwd_save():
    if entry_web.get() == "" or entry_web.get() == "" or entry_web.get() == "":
        messagebox.showerror("Oops!",
                             "Error: one of following is missing:\n 1) website,\n 2) email/username\n 3) password")
    else:
        with open("pwds.csv", encoding="utf-8", mode="a", newline="\n") as file:
            pwd_file = csv.writer(file)
            new_entry = [entry_web.get(),
                         entry_user.get(),
                         entry_pwd.get()]
            pwd_file.writerow(new_entry)
            # remove website and password written values after adding into
            entry_web.delete(0, END)
            entry_pwd.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# ✔TODO: fix grid problem with 2 fields next to eachother while text fields are over multiple columns
win = Tk()
win.title("Password Manager")
win.config(padx=40, pady=40)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web = Label(text="Website:", font=FONT)
web.grid(column=0, row=1)

user = Label(text="Email/Username:", font=FONT)
user.grid(column=0, row=2)

pwd = Label(text="Password:", font=FONT)
pwd.grid(column=0, row=3)

# Text fields
entry_web = Entry(width=35, font=FONT)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

entry_user = Entry(width=35, font=FONT)
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.insert(0, "your_mail@domain.com")

entry_pwd = Entry(width=17, font=FONT)
entry_pwd.grid(column=1, row=3)

# Buttons
add = Button(text="Add", width=35, font=FONT, command=pwd_save)
add.grid(column=1, row=4, columnspan=2)

generate = Button(text="Generate Password", width=17,
                  font=FONT, command=pwd_gen)
generate.grid(column=2, row=3)

win.mainloop()

# TODO: later on change GUI to be more modern
