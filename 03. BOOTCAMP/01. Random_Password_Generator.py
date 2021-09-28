import random


def sorteia(v1, v2, v3):
    """
    :param v1: INT
    :param v2: INT
    :param v3: INT
    :return: STRING
    """
    password = ''
    for i in range(0, v1):
        password += random.choice(letters)
    for i in range(0, v2):
        password += random.choice(symbols)
    for i in range(0, v3):
        password += random.choice(numbers)
    password = ''.join(random.sample(password, len(password)))
    return password


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw = sorteia(nr_letters, nr_symbols, nr_numbers)

print(f'Your Password is "{pw}"')
