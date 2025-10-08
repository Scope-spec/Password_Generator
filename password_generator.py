import string
import secrets

chart = string.ascii_letters + string.digits + string.punctuation

def main():
    try:
        while True:
            length = int(input("Your password length: "))
            if length < 6:
                print("Too short password (min 6 characters)")
            else: break

        while True:
            password = "".join(secrets.choice(chart) for i in range(length))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password) >= 2):
                break

        print("This is your password:")
        print(password)

    except ValueError:
        print("Not an integer")

if __name__ == "__main__":
    main()



