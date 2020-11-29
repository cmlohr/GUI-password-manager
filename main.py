from tkinter import *
import pass_chars
import random

# CONST
BLACK = "#191919"
RED = "#f05454"
GREY = "#495464"
TEXT = "#dbf6e9"
FONT = ("Roboto", 12, "normal")


# Password Generator
def gen_pass():
    picked_chars = []
    picked_chars += random.choices(pass_chars.letters, k=10)
    picked_chars += random.choices(pass_chars.symbols, k=3)
    picked_chars += random.choices(pass_chars.numbers, k=3)
    random.shuffle(picked_chars)
    my_pass = ''.join([str(item) for item in picked_chars])
    password_input_output.insert(0, f"{my_pass}")


# Saves Password info to data.txt
def add_pass():
    with open("data.txt", mode="a") as data:
        data.write(f"{website_input.get()} | {email_username_input.get()} | {password_input_output.get()}\n")


# GUI
wd = Tk()
wd.title("Password Manager")
wd.config(padx=20, pady=20, bg=BLACK)
can = Canvas(height=200, width=210, bg=BLACK, highlightthickness=0)
lock_img = PhotoImage(file="my_lock.png")
can.create_image(130, 80, image=lock_img)  # the tuple defines the x and y
can.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:", bg=BLACK, fg=TEXT, font=FONT)
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/User:", bg=BLACK, fg=TEXT, font=FONT)
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=BLACK, fg=TEXT, font=FONT)
password_label.grid(column=0, row=3)

# ENTRY
website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_username_input = Entry(width=36)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "email@mail.com")
password_input_output = Entry(width=21)
password_input_output.grid(column=1, row=3)

# BUTTONS
gen_pass_btn = Button(width=12, text="Generate", bg=GREY, fg=TEXT, activebackground=RED, command=gen_pass)
gen_pass_btn.grid(column=2, row=3)
add_pass_btn = Button(width=34, text="Add Password", bg=GREY, fg=TEXT, activebackground=RED, command=add_pass)
add_pass_btn.grid(column=1, row=4, columnspan=2)

wd.mainloop()
