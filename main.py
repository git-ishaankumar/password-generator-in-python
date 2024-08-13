# imported modules
import sys
import random

# functions
def generate(length, format):  # generate password
    potential_characters = []
    password = ""
    for i in range(length):
        if '1' in format:
            potential_characters.append(1)
        if '2' in format:
            potential_characters.append(2)
        if '3' in format:
            potential_characters.append(3)
        if '4' in format:
            potential_characters.append(4)
        random_choice = random.choice(potential_characters)
        if random_choice == 1:
            password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # uppercase letters
        elif random_choice == 2:
            password += random.choice("abcdefghijklmnopqrstuvwxyz")  # lowercase letters
        elif random_choice == 3:
            password += random.choice("0123456789")  # numbers
        elif random_choice == 4:
            password += random.choice("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")  # symbols

    return password


def ask():
    # user input
    def length():
        try:
            password_length_ask = int(input("\nEnter the length of your 1-50 character password (or enter 0 to quit):\n"))
            if password_length_ask == 0:
                sys.exit()
            if password_length_ask < 1 or password_length_ask > 50:
                print("Please enter an integer value from 1-50.")
                return length()
            else:
                return password_length_ask
        except ValueError:
            print("Please enter an integer value from 1-50.")
            return length()

    def format():
        format_ask = input("\nEnter the type of characters that should be in the password. To choose multiple, type multiple numbers (e.g. \"134\")\n1.) Uppercase\n2.) Lowercase\n3.) Numbers\n4.) Symbols\n\n")
        if not set(format_ask).issubset({'1', '2', '3', '4'}):
            print("Please enter either 1, 2, 3, or 4")
            return format()
        else:
            return format_ask

    password_length = length()
    password_format = format()

    password = generate(password_length, password_format)
    return password

# main/body
while True:
    password = ask()
    print(f"\nCopy ======>\t\t{password}\t\t<====== Copy")
