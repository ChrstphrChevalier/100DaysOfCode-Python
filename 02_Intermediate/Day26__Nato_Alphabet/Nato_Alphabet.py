#TODO 1. Create a dictionary in this format:

import csv

with open("nato_phonetic_alphabet.csv", newline='')as f:
    reader = csv.DictReader(f)
    data = {row['letter']: row['code'] for row in reader}
    


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    codeName = []
    word = input("What's your name ?: ").upper()
    if word.isalpha():
        for letter in word:
            codeName.append(data[letter])
    else:
        print("Invalid name.")
        continue
    print(codeName)
    restart = input("This repl has exited. Run again ?(Y/N): ").upper()
    if restart != 'Y':
        break