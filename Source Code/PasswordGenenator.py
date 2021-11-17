import random

# Lists of characters
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
let = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cha = ["!", "@", "/", "#", "$", "%", "&", "*", "ç", "(", ")"]
size = 0

repeat_request = False

# All configs are false by adefault
num_request = "n"
let_request = "n"
cha_request = "n"

# Statements for each while
a = True
b = True
c = True
d = True
e = True
f = True

# To check if the user chose at least one of the criteria
criteria = 0

while f == True:
    while a == True:
        num_request = input("Do you want numbers?(Y/N) ")
        num_request = num_request.lower()
        if num_request == "y" or num_request == "n":
            print("You chose:", num_request)
            a = False
            if num_request == "y":
                criteria += 1
        else:
            print("Invalid character, please type Y or N")

    while b == True:
        let_request = input("Do you want letters?(Y/N) ")
        let_request = let_request.lower()
        if let_request == "y" or let_request == "n":
            print("You chose:", let_request)
            b = False
            if let_request == "y":
                criteria += 1
        else:
            print("Invalid character, please type Y or N")

    while c == True:
        cha_request = input("Do you want especial characters?(Y/N) ")
        cha_request = cha_request.lower()
        if cha_request == "y" or cha_request == "n":
            print("You chose:", cha_request)
            c = False
            if cha_request == "y":
                criteria += 1
        else:
            print("Invalid character, please type Y or N")

    # Checking if the user chose any of the criteria
    if criteria > 0:
        f = False
    else:
        print("Please enter at least one criteria")

    a = True
    b = True
    c = True

while d == True:
    repeat_request = input("Do you want characters to be able to repeat?(Y/N) ")
    if repeat_request == "y" or repeat_request == "n":
        print("You chose:", repeat_request)
        d = False
    else:
        print("Invalid character, please type Y or N")

password = []
ammount = 0
if num_request == "y":
    password.extend(num)
    ammount += len(num)
if let_request == "y":
    password.extend(let)
    ammount += len(let)
if cha_request == "y":
    password.extend(cha)
    ammount+= len(cha)

while e == True:
    size = input("Choose a size for your password: ")
    try:
        size = int(size)
        if size <= 0:
            print("Not enough characters")
        if repeat_request == "y":
            e = False
        else:
            if size > ammount:
                print("Please choose a smaller number, it's not possible to\nmake a password this long without repeating a characters")
            else:
                e = False
    except ValueError:
        print("Please insert an integer number")

random.shuffle(password)

key = ""
key_list = []
choice = ""

#if it can repeat
if repeat_request == "y":
    for i in range(size):
        key = key + str(random.choices(password))
    
#if it can't repeat
else:
    for j in range(size):
        choice = random.choices(password)
        key_list.extend(choice[0])
        password.remove(choice[0])
    for h in range(len(key_list)):
        key = key + str(key_list[h])

print(key.replace("[", "").replace("]", "").replace(" ", "").replace("'", ""))