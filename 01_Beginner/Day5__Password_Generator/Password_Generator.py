import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for _ in range(nr_letters):
    password += letters[random.randint(0,51)]
for _ in range(nr_symbols):
    password += symbols[random.randint(0,8)]
for _ in range(nr_numbers):
    password += numbers[random.randint(0,9)]

print(f"Password by EasyMethod : {password}")

high_password = []

for _ in range(nr_letters):
    high_password.append(letters[random.randint(0,51)])
for _ in range(nr_symbols):
    high_password.append(symbols[random.randint(0,8)])
for _ in range(nr_numbers):
    high_password.append(numbers[random.randint(0,9)])

random.shuffle(high_password)
password = ''.join(high_password)
print(f"Password by HardMethod : {password}")