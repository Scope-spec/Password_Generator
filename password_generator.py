import random

letters = "abcdefghijklmnoupqrstvwxyzh"
numbers = "0123456789"
special = "!#-_."
chart = letters + numbers + special

try:
    length = int(input("Password length: "))
    password = ""
    for _ in range(length):
        password += random.choice(chart)
    
    print("This is your password: ")
    print(password)
except:
    print("Not integer!")

