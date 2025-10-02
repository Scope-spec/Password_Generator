import random

letters = "abcdefghijklmnoupqrstvwxyzh"
numbers = "0123456789"
special = "!#-_."
chart = letters + numbers + special

def main():
    length = int(input("Your password length: "))
    password = ""
    for _ in range(length):
        letter = random.choice(chart)
        password += letter
    
    print("This is your password:")
    print(password)

if __name__ == "__main__":
    main()


