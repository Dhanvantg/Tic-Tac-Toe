#Tic Tac Toe
#Author : Danniboy07
import os
import random
import time
nos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
print("This is the layout of the Puzzle, please enter the number appropriate to the box you want to fill in")
print("      1" + " / " + "2" + " / " + "3")
print("    -----------")
print("    4" + " / " + "5" + " / " + "6")
print("  -----------")
print("  7" + " / " + "8" + " / " + "9")
def board():
    print("      " + str(a) + " / " + str(b) + " / " + str(c))
    print("    -----------")
    print("    " + str(d) + " / " + str(e) + " / " + str(f))
    print("  -----------")
    print("  " + str(g) + " / " + str(h) + " / " + str(i))
time.sleep(1)
user = input("where would you fill X in?: ")
if user == "1":
    a = "X"
elif user == "2":
    b = "X"
elif user == "3":
    c = "X"
elif user == "4":
    d = "X"
elif user == "5":
    e = "X"
elif user == "6":
    f = "X"
elif user == "7":
    g = "X"
elif user == "8":
    h = "X"
elif user == "9":
    i = "X"
else:
    print("Invalid Input, please enter the number corresponding to the box")
    user = input("where would you fill X in?: ")
    if user == "1":
        a = "X"
    elif user == "2":
        b = "X"
    elif user == "3":
        c = "X"
    elif user == "4":
        d = "X"
    elif user == "5":
        e = "X"
    elif user == "6":
        f = "X"
    elif user == "7":
        g = "X"
    elif user == "8":
        h = "X"
    elif user == "9":
        i = "X"
    else:
        print("Failed attempts more than 1... Quitting")
        time.sleep(1.5)
        exit()
nos.remove(user)
board()
time.sleep(1)
bot = random.choice(nos)
if bot == "1":
    a = "O"
elif bot == "2":
    b = "O"
elif bot == "3":
    c = "O"
elif bot == "4":
    d = "O"
elif bot == "5":
    e = "O"
elif bot == "6":
    f = "O"
elif bot == "7":
    g = "O"
elif bot == "8":
    h = "O"
elif bot == "9":
    i = "O"
else:
    print("Invalid Input, please enter the number corresponding to the box")
print("Generating Bot input....")
nos.remove(bot)
time.sleep(1)
board()
time.sleep(1)
#-------------------------------------------User 2---------------------------------------------------------

user2 = input("where would you fill your X in?: ")
if user2 == user or user2 == bot:
    print("please dont repeat values")
    user2 = input("where would you fill your X in?")
    if user2 == user or user2 == bot:
        print("Final warning before the game ends")
        user2 = input("where would you fill your X in?")
        if user2 == user or user2 == bot:
            exit()
nos.remove(user2)
if user2 == "1":
    a = "X"
elif user2 == "2":
    b = "X"
elif user2 == "3":
    c = "X"
elif user2 == "4":
    d = "X"
elif user2 == "5":
    e = "X"
elif user2 == "6":
    f = "X"
elif user2 == "7":
    g = "X"
elif user2 == "8":
    h = "X"
elif user2 == "9":
    i = "X"
else:
    print("Invalid input, please enter the number corresponding to the box")
    user2 = input("where would you fill your X in?: ")
    if user2 == "1":
        a = "X"
    elif user2 == "2":
        b = "X"
    elif user2 == "3":
        c = "X"
    elif user2 == "4":
        d = "X"
    elif user2 == "5":
        e = "X"
    elif user2 == "6":
        f = "X"
    elif user2 == "7":
        g = "X"
    elif user2 == "8":
        h = "X"
    elif user2 == "9":
        i = "X"
    else:
        i = "X"
        print("Too many failed attempts, quitting")
        time.sleep(1.5)
        exit()
time.sleep(1)
board()
bot2 = random.choice(nos)
time.sleep(1)
if a == b == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot2 = 0
elif b == c == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot2 = 0
elif d == e == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot2 = 0
elif e == f == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot2 = 0
elif g == h == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot2 = 0
elif h == i == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot2 = 0
elif a == d == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot2 = 0
elif d == g == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot2 = 0
elif b == e == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot2 = 0
elif e == h == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot2 = 0
elif c == f == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot2 = 0
elif i == f == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot2 = 0
elif a == e == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot2 = 0
elif i == e == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot2 = 0
elif g == e == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot2 = 0
elif e == c == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot2 = 0
elif a == g == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot2 = 0
elif b == h == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot2 = 0
elif c == i == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot2 = 0
elif a == c == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot2 = 0
elif d == f == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot2 = 0
elif g == i == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot2 = 0
else:
    try:
        nos.remove(bot2)
    except Exception:
        pass
    if bot2 == "1":
        a = "O"
    elif bot2 == "2":
        b = "O"
    elif bot2 == "3":
        c = "O"
    elif bot2 == "4":
        d = "O"
    elif bot2 == "5":
        e = "O"
    elif bot2 == "6":
        f = "O"
    elif bot2 == "7":
        g = "O"
    elif bot2 == "8":
        h = "O"
    elif bot2 == "9":
        i = "O"
    else:
        print("Invalid Input, please enter the number corresponding to the box")
print("loading...")
board()
user3 = input("where would you fill your X in?: ")
if user3 == user or user3 == user2 or user3 == bot or user3 == bot2:
    print("please dont repeat values")
    user3 = input("where would you fill your X in?")
    if user3 == user or user3 == user2 or user3 == bot or user3 == bot2:
        print("Final warning before the game ends")
        user3 = input("where would you fill your X in?")
        if user3 == user or user3 == user2 or user3 == bot or user3 == bot2:
            exit()
nos.remove(user3)
if user3 == "1":
    a = "X"
elif user3 == "2":
    b = "X"
elif user3 == "3":
    c = "X"
elif user3 == "4":
    d = "X"
elif user3 == "5":
    e = "X"
elif user3 == "6":
    f = "X"
elif user3 == "7":
    g = "X"
elif user3 == "8":
    h = "X"
elif user3 == "9":
    i = "X"
else:
    print("Invalid input, Please try again: ")
    user3 = input("where would you fill your X in?: ")
    if user3 == "1":
        a = "X"
    elif user3 == "2":
        b = "X"
    elif user3 == "3":
        c = "X"
    elif user3 == "4":
        d = "X"
    elif user3 == "5":
        e = "X"
    elif user3 == "6":
        f = "X"
    elif user3 == "7":
        g = "X"
    elif user3 == "8":
        h = "X"
    elif user3 == "9":
        i = "X"
    else:
        print("Too many failed attempts, quitting")
        time.sleep(1.5)
        exit()
if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    board()
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    board()
    time.sleep(10)
    exit()
board()
time.sleep(1)
bot3 = random.choice(nos)
if a == b == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot3 = 0
elif b == c == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot3 = 0
elif d == e == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot3 = 0
elif e == f == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot3 = 0
elif g == h == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot3 = 0
elif h == i == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot3 = 0
elif a == d == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot3 = 0
elif d == g == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot3 = 0
elif b == e == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot3 = 0
elif e == h == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot3 = 0
elif c == f == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot3 = 0
elif i == f == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot3 = 0
elif a == e == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot3 = 0
elif i == e == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot3 = 0
elif g == e == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot3 = 0
elif e == c == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot3 = 0
elif a == g == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot3 = 0
elif b == h == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot3 = 0
elif c == i == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot3 = 0
elif a == c == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot3 = 0
elif d == f == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot3 = 0
elif g == i == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot3 = 0
else:
    try:
        nos.remove(bot3)
    except Exception:
        pass
    if bot3 == "1":
        a = "O"
    elif bot3 == "2":
        b = "O"
    elif bot3 == "3":
        c = "O"
    elif bot3 == "4":
        d = "O"
    elif bot3 == "5":
        e = "O"
    elif bot3 == "6":
        f = "O"
    elif bot3 == "7":
        g = "O"
    elif bot3 == "8":
        h = "O"
    elif bot3 == "9":
        i = "O"
    else:
        print("Invalid Input, please enter the number corresponding to the box")
board()
if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    time.sleep(10)
    exit()

#-------------------------------------------User 4---------------------------------------------------------
user4 = input("where would you fill your X in?: ")
if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
    print("please dont repeat values")
    user4 = input("where would you fill your X in?: ")
    if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
        print("Final warning before the game ends")
        user4 = input("where would you fill your X in?: ")
        if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
            exit()
if user4 == "1":
    a = "X"
elif user4 == "2":
    b = "X"
elif user4 == "3":
    c = "X"
elif user4 == "4":
    d = "X"
elif user4 == "5":
    e = "X"
elif user4 == "6":
    f = "X"
elif user4 == "7":
    g = "X"
elif user4 == "8":
    h = "X"
elif user4 == "9":
    i = "X"
else:
    print("Invalid input, please enter a number corresponding to the box")
    user4 = input("where would you fill your X in?")
    if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
        print("please dont repeat values")
        user4 = input("where would you fill your X in?")
        if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
            print("Final warning before the game ends")
            user4 = input("where would you fill your X in?")
            if user4 == user or user4 == user2 or user4 == user3 or user4 == bot or user3 == bot2 or user4 == bot3:
                exit()
    if user4 == "1":
        a = "X"
    elif user4 == "2":
        b = "X"
    elif user4 == "3":
        c = "X"
    elif user4 == "4":
        d = "X"
    elif user4 == "5":
        e = "X"
    elif user4 == "6":
        f = "X"
    elif user4 == "7":
        g = "X"
    elif user4 == "8":
        h = "X"
    elif user4 == "9":
        i = "X"
    else:
        print("Too many failed attempts, quitting")
        time.sleep(1.5)
        exit()
if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    board()
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    board()
    time.sleep(10)
    exit()
else:
    time.sleep(1)
bot4 = random.choice(nos)
if a == b == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot4 = 0
elif b == c == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot4 = 0
elif d == e == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot4 = 0
elif e == f == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot4 = 0
elif g == h == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot4 = 0
elif h == i == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot4 = 0
elif a == d == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot4 = 0
elif d == g == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot4 = 0
elif b == e == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot4 = 0
elif e == h == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot4 = 0
elif c == f == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot4 = 0
elif i == f == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot4 = 0
elif a == e == "X" and i == 9:
    i = "O"
    nos.remove("9")
    bot4 = 0
elif i == e == "X" and a == 1:
    a = "O"
    nos.remove("1")
    bot4 = 0
elif g == e == "X" and c == 3:
    c = "O"
    nos.remove("3")
    bot4 = 0
elif e == c == "X" and g == 7:
    g = "O"
    nos.remove("7")
    bot4 = 0
elif a == g == "X" and d == 4:
    d = "O"
    nos.remove("4")
    bot4 = 0
elif b == h == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot4 = 0
elif c == i == "X" and f == 6:
    f = "O"
    nos.remove("6")
    bot4 = 0
elif a == c == "X" and b == 2:
    b = "O"
    nos.remove("2")
    bot4 = 0
elif d == f == "X" and e == 5:
    e = "O"
    nos.remove("5")
    bot4 = 0
elif g == i == "X" and h == 8:
    h = "O"
    nos.remove("8")
    bot4 = 0
elif a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    board()
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    board()
    time.sleep(10)
    exit()
else:
    try:
        nos.remove(bot4)
    except Exception:
        pass
    if bot4 == "1":
        a = "O"
    elif bot4 == "2":
        b = "O"
    elif bot4 == "3":
        c = "O"
    elif bot4 == "4":
        d = "O"
    elif bot4 == "5":
        e = "O"
    elif bot4 == "6":
        f = "O"
    elif bot4 == "7":
        g = "O"
    elif bot4 == "8":
        h = "O"
    elif bot4 == "9":
        i = "O"
    else:
        print("Invalid Input, please enter the number corresponding to the box")
board()
if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    time.sleep(10)
    exit()
#-------------------------------------------User 5---------------------------------------------------------
user5 = input("where would you fill your X in?: ")
if user5 == user or user5 == user2 or user5 == user3 or user5 == user4 or user5 == bot or user5 == bot2 or user5 == bot3 or user5 == bot4:
    print("please dont repeat values")
    user2 = input("where would you fill your X in?")
    if user5 == user or user5 == user2 or user5 == user3 or user5 == user4 or user5 == bot or user5 == bot2 or user5 == bot3 or user5 == bot4:
        print("Final warning before the game ends")
        user2 = input("where would you fill your X in?")
        if user5 == user or user5 == user2 or user5 == user3 or user5 == user4 or user5 == bot or user5 == bot2 or user5 == bot3 or user5 == bot4:
            exit()
nos.remove(user5)
if user5 == "1":
    a = "X"
elif user5 == "2":
    b = "X"
elif user5 == "3":
    c = "X"
elif user5 == "4":
    d = "X"
elif user5 == "5":
    e = "X"
elif user5 == "6":
    f = "X"
elif user5 == "7":
    g = "X"
elif user5 == "8":
    h = "X"
elif user5 == "9":
    i = "X"
else:
    print("Invalid input, please enter a number corresponding to the box")
    user5 = input("where would you fill your X in?: ")
board()
if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" or a == d == g == "X" or b == e == h == "X" or c == f == i == "X" or a == e == i == "X" or g == e == c == "X":
    print("You Win!! Congratulations!")
    time.sleep(10)
    exit()
elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" or a == d == g == "O" or b == e == h == "O" or c == f == i == "O" or a == e == i == "O" or g == e == c == "O":
    print("You lose :(")
    time.sleep(10)
    exit()
else:
    print("Its a Draw")
    time.sleep(10)
    exit()
#By Danny
