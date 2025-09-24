import random

letters = "abcdefghijklmnoupqrstvwxyzh"
numbers = "0123456789"
special = "!#-_."
chart = letters + numbers + special

password = ""
for _ in range(16):
    password += random.choice(chart)
    
print("This is your password: ")
print(password)