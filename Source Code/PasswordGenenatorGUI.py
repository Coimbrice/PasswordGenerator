import random
import string
from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("Password Generator")
#root.iconbitmap("assets/keyHole2.ico")
root.resizable(width=False, height=False)

# Minimum size a password can be depending on what is marked
# if all boxes selected, the password shaw be at least 4 char long
minimum = 1
maximum = 30
criteria = 0
password = ""
cha = ["!", "@", "/", "\\", "#", "$", "%", "&", "*", "ç", "(", ")", "[", "]", "{", "}", "+", "-"] 

checkboxes = Frame(root)
checkboxes.pack(pady = 0)

num = IntVar()
a = Checkbutton(checkboxes, text = "Numbers", variable = num, onvalue = 1, offvalue = 0,\
    font = "HELVETICA 14", anchor="e")
a.grid(row = 0, column = 0, sticky='w')

spec = IntVar()
b = Checkbutton(checkboxes, text = "Special Characters", variable = spec, onvalue = 1,\
    offvalue = 0, font = "HELVETICA 14")
b.grid(row = 0, column = 1, sticky='w')

low = IntVar()
c = Checkbutton(checkboxes, text = "Lowercase Letters", variable = low, onvalue = 1,\
    offvalue = 0, font = "HELVETICA 14")
c.grid(row = 1, column = 0, sticky='w')

upp = IntVar()
d = Checkbutton(checkboxes, text = "Uppercase Letters", variable = upp, onvalue = 1,\
    offvalue = 0, font = "HELVETICA 14")
d.grid(row = 1, column = 1, sticky='w')

rep = IntVar()
e = Checkbutton(checkboxes, text = "Don't repeat characters", variable = rep, onvalue = 1,\
    offvalue = 0, font = "HELVETICA 14")
e.grid(row = 2, column = 0)

DisplayLabel = LabelFrame(root, text = "Password", font = "HELVETICA 15")
DisplayLabel.pack(pady = 10)
DisplayPassword = Entry(DisplayLabel, text = "", font = ("Helvetica", 24), bd = 3, bg = "WHITE")
DisplayPassword.pack(pady = 10)

line5 = Frame(root)
line5.pack(pady = 0, padx = 10)
slider = Scale(line5, from_ = minimum, to = maximum, length = 150, orient = HORIZONTAL,\
    activebackground = "#d3d3d3", font = "HELVETICA 12")
slider.grid(row = 0, column = 0)

def slider_range():
    # Slider minimum
    checked = upp.get() + low.get() + num.get() + spec.get()
    if checked > 0:
        minimum = checked
        slider.config(from_ = minimum)
    else:
        minimum = 1
        slider.config(from_ = minimum)

    # Slider maximum
    if rep.get() > 0:
        if upp.get() + low.get() == 1 and num.get() + spec.get() == 0:
            maximum = 26
            slider.config(to = maximum)
        elif num.get() == 1 and spec.get() + upp.get() + low.get() == 0:
            maximum = 10
            slider.config(to = maximum)
        elif spec.get() == 1 and num.get() + upp.get() + low.get() == 0:
            maximum = 18
            slider.config(to = maximum)
        elif spec.get() + num.get() == 2 and upp.get() + low.get() == 0:
            maximum = 28
            slider.config(to = maximum)
        else:
            maximum = 30
            slider.config(to = maximum)
    else:
        maximum = 30
        slider.config(to = maximum)

a.config(command = slider_range)
b.config(command = slider_range)
c.config(command = slider_range)
d.config(command = slider_range)
e.config(command = slider_range)

# warns the user about missing criteria
line6 = Frame(root)
line6.pack(pady = 0, padx = 10)
warn_user = Label(line6, text = "", fg = "RED")
warn_user.pack(pady=10)

# copy password to your clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(DisplayPassword.get())

# whole process of creating a password based on user input
def generate():
    num_used = ""
    upp_used = ""
    low_used = ""
    spec_used = ""

    minimum = num.get() + spec.get() + upp.get() + low.get()

    if num.get() + spec.get() + upp.get() + low.get() + rep.get() > 0:
        if rep.get() > 0 and num.get() + spec.get() + upp.get() + low.get() < 1:
            warn_user.config(text = "Please choose at least 1 more criteria")
        else:
            warn_user.config(text = "")
            password_chars = ""

            # if the characters can repeat
            if rep.get() < 1:
                portion = (slider.get()//minimum)
                while len(password_chars) < slider.get():
                    if upp.get() > 0:
                        for i in range(random.randint(1, portion)):
                            letter = random.choice(string.ascii_letters)
                            password_chars += letter.upper()
                    if low.get() > 0:
                        for j in range(random.randint(1, portion)):
                            letter = random.choice(string.ascii_letters)
                            password_chars += letter.lower()
                    if num.get() > 0:
                        for k in range(random.randint(1, portion)):
                            password_chars += str(random.randint(0, 9))
                    if spec.get() > 0:
                        for l in range(random.randint(1, portion)):
                            password_chars += random.choice(cha)
                while len(password_chars) > slider.get():
                    password_chars = password_chars[:-1]
                
                generated = ''.join(random.sample(password_chars,\
                    len(password_chars)))

                DisplayPassword.delete(0, END)
                DisplayPassword.insert(0, generated)

            else:
                # Characters won't repeat
                password_chars = ""
                portion = (slider.get()//minimum)
                while len(password_chars) < slider.get():
                    if upp.get() > 0:
                        for i in range(random.randint(1, portion)):
                            a = 0
                            while a == 0:
                                letter = random.choice(string.ascii_letters)
                                letter = letter.upper()
                                if str(letter) not in password_chars:
                                    password_chars += letter.upper()
                                    upp_used += letter
                                    a = 1
                                elif len(upp_used) >= 26:
                                    a = 1
                                elif len(password_chars) >= 26 and num.get() +\
                                    low.get() + spec.get() == 0:
                                    a = 1
                    if low.get() > 0:
                        for j in range(random.randint(1, portion)):
                            a = 0
                            while a == 0:
                                letter = random.choice(string.ascii_letters)
                                letter = letter.lower()
                                if str(letter) not in password_chars:
                                    password_chars += letter.lower()
                                    low_used += letter
                                    a = 1
                                elif len(low_used) >= 26:
                                    a = 1
                                elif len(password_chars) >= 26 and num.get() +\
                                    upp.get() + spec.get() == 0:
                                    a = 1
                    if num.get() > 0:
                        for k in range(random.randint(1, portion)):
                            a = 0
                            while a == 0:
                                letter = str(random.randint(0, 9))
                                if letter not in password_chars:
                                    password_chars += str(letter)
                                    num_used += letter
                                    a = 1
                                elif len(num_used) >= 10:
                                    a = 1
                                elif len(password_chars) >= 9 and upp.get() +\
                                    low.get() + spec.get() == 0:
                                    a = 1  
                    if spec.get() > 0:
                        for l in range(random.randint(1, portion)):
                            a = 0
                            while a == 0:
                                letter = str(random.choice(cha))
                                if letter not in password_chars:
                                    password_chars += str(letter)
                                    spec_used += letter
                                    a = 1
                                elif len(spec_used) >= 18:
                                    a = 1
                                elif len(password_chars) >= 18 and upp.get() +\
                                    low.get() + num.get() == 0:
                                    a = 1

                while len(password_chars) > slider.get():
                    password_chars = password_chars[:-1]
                
                generated = ''.join(random.sample(password_chars,\
                    len(password_chars)))

                DisplayPassword.delete(0, END)
                DisplayPassword.insert(0, generated)        
                
    else:
        warn_user.config(text = "Please choose at least 1 criteria")

buttonGen = Button(line5, text = "Copy", command = copy)
buttonGen.config(font=("HELVETICA", 13, "bold"))
buttonGen.grid(row = 0, column = 1, pady = 0, padx = 10)

buttonGen = Button(line5, text = "Generate", command = generate)
buttonGen.config(font=("HELVETICA", 13, "bold"))
buttonGen.grid(row = 0, column = 2, pady = 0, padx = 10)

root.mainloop()