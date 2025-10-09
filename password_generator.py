import string
import secrets

chart = string.ascii_letters + string.digits + string.punctuation

def user_input():
    while True:
        user_input = input("Your password length: ")

        if user_input.isdigit():
            length = int(user_input)
            if length < 6:
                print("Too short password (min 6 characters)")
            else:
                return length
        else: 
            print("Not an integer. Please enter a whole number.")

def main(n):
    while True:
        password = "".join(secrets.choice(chart) for i in range(n))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 2):
            break

    print("This is your password:")
    print(password)


if __name__ == "__main__":
    u_input = user_input()
    main(u_input)


