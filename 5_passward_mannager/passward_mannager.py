
from cryptography.fernet import Fernet
import os

# Run this function only once to generate a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Create the key if it doesn't exist
if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)


def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return

    with open("passwords.txt", "r") as f:
        for line in f:
            data = line.rstrip()

            if "|" not in data:
                continue

            user, passw = data.split("|", 1)

            try:
                decrypted_password = fer.decrypt(
                    passw.encode()
                ).decode()

                print("Account:", user, "| Password:", decrypted_password)

            except Exception:
                print("Could not decrypt password for:", user)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_password = fer.encrypt(pwd.encode()).decode()

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_password + "\n")

    print("Password saved successfully!")


while True:
    mode = input(
        "Would you like to add or view passwords? "
        "(add/view/q to quit): "
    ).lower().strip()

    if mode == "q":
        print("Goodbye!")
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode. Please enter add, view, or q.")
