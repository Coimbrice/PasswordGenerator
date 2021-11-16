import random
import string
from tkinter import *
from PIL import ImageTk, Image

# AVISO DE CRITERIA
# ALINHAR SLIDER E BOTOES
# FUNCIONALIDADE DONT REPEAT

root = Tk()
root.geometry("450x300")
root.title("Password Generator")
root.iconbitmap("assets/keyHole.ico")
root.resizable(width=False, height=False)

# Minimum size a password can be depending on what is marked
# if all boxes selected, the password shaw be at least 4 char long
minimun = 4
criteria = 0
password = ""
cha = ["!", "@", "/", "\\", "#", "$", "%", "&", "*", "ç", "(", ")", "[", "]", "{", "}", "+", "-"]

checkboxes = Frame(root)
checkboxes.pack(pady = 0)

num = IntVar()
a = Checkbutton(checkboxes, text = "Numbers", variable = num, onvalue = 1, offvalue = 0, font = "HELVETICA 14", anchor="e")
a.grid(row = 0, column = 0, sticky='w')

spec = IntVar()
b = Checkbutton(checkboxes, text = "Special Characters", variable = spec, onvalue = 1, offvalue = 0, font = "HELVETICA 14")
b.grid(row = 0, column = 1, sticky='w')

low = IntVar()
c = Checkbutton(checkboxes, text = "Lowercase Letters", variable = low, onvalue = 1, offvalue = 0, font = "HELVETICA 14")
c.grid(row = 1, column = 0, sticky='w')

upp = IntVar()
d = Checkbutton(checkboxes, text = "Uppercase Letters", variable = upp, onvalue = 1, offvalue = 0, font = "HELVETICA 14")
d.grid(row = 1, column = 1, sticky='w')

rep = IntVar()
e = Checkbutton(checkboxes, text = "Don't repeat characters", variable = rep, onvalue = 1, offvalue = 0, font = "HELVETICA 14")
e.grid(row = 2, column = 0)

DisplayLabel = LabelFrame(root, text = "Password", font = "HELVETICA 15")
DisplayLabel.pack(pady = 10)
DisplayPassword = Entry(DisplayLabel, text = "", font = ("Helvetica", 24), bd = 3, bg = "WHITE")
DisplayPassword.pack(pady = 10)

line5 = Frame(root)
line5.pack(pady = 0, padx = 10)
slider = Scale(line5, from_ = minimun, to = 30, length = 150, orient = HORIZONTAL,\
    activebackground = "#d3d3d3", font = "HELVETICA 12")
slider.grid(row = 0, column = 0)

line6 = Frame(root)
line6.pack(pady = 0, padx = 10)

# copy password to your clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(DisplayPassword.get())

# whole process of creating a password based on user input
def generate():
    '''global one_criteira
    #one_criteria = "Choose at least 1 criteria"
    #global onemore_criteria
    #onemore_criteria = "Choose at least 1 more criteria"
    #global size_criteria
    #size_criteria = "Choose a smaller password size if you don't want characters to repeat"
    # '''

    minimun = num.get() + spec.get() + upp.get() + low.get()
    if num.get() + spec.get() + upp.get() + low.get() + rep.get() > 0:
        if rep.get() > 0 and num.get() + spec.get() + upp.get() + low.get() < 1:
            print("onemore_criteria")
        else:
            password_chars = ""

            # if the characters can repeat
            if rep.get() < 1:
                portion = (slider.get()//minimun)
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
                print(password_chars)
                
                generated = ''.join(random.sample(password_chars, len(password_chars)))

                
                DisplayPassword.delete(0, END)
                DisplayPassword.insert(0, generated)

            else:
                print("dont repeat")
                portion = (slider.get()//minimun)
                while len(password_chars) < slider.get():
                    if upp.get() > 0:
                        for i in range(random.randint(1, portion)):
                            letter = random.choice(string.ascii_letters)
                            while letter in password_chars:
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
                    generated = password_chars  
                DisplayPassword.delete(0, END)
                DisplayPassword.insert(0, generated)         
                
    else:
        print("one_criteria")

buttonGen = Button(line5, text = "Copy", command = copy)
buttonGen.config(font=("HELVETICA", 13, "bold"))
buttonGen.grid(row = 0, column = 1, pady = 0, padx = 10)

buttonGen = Button(line5, text = "Generate", command = generate)
buttonGen.config(font=("HELVETICA", 13, "bold"))
buttonGen.grid(row = 0, column = 2, pady = 0, padx = 10)


root.mainloop()