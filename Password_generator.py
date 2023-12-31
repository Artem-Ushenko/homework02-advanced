import string
import random

def generator_password(length_password):
    all_symbols = string.ascii_letters + string.digits + string.punctuation

    condition = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
                 random.choice(string.digits), random.choice(string.punctuation)]

    password = random.sample(condition, len(condition)) + random.sample(all_symbols, length_password - len(condition))

    random.shuffle(password)

    return ''.join(password)


try:
    print("Welcome to the Linux User Password Generator!")

    length_password = int(input("Please enter the desired password length: "))
    if length_password < 4:
        print("Please enter length a greater than 4 symbols to make the password stronger !!!")
    else:
        print("Your password: ", generator_password(length_password))
except ValueError:
    print("Incorrect input !!! Please enter true length for password !!!")

