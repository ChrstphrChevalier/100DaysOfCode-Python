import string
import art

print(art.logo)


alphabet = list(string.ascii_lowercase)
def encrypt(original_text, shift_amount):
    hide_word = "".join(alphabet[(alphabet.index(c) + shift_amount) % len(alphabet)] if c in alphabet else c for c in original_text)
    print(hide_word)

def decrypt(original_text, shift_amount):
    reveal_word = "".join(alphabet[(alphabet.index(c) - shift_amount) % len(alphabet)] if c in alphabet else c for c in original_text)
    print(reveal_word)

def caesar(original_text, shift_amount, action):
    if action == "encode":
        encrypt(original_text, shift_amount)
    elif action == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Type Error")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, action=direction)
    again = input("Do you want to continue? (yes/no):\n").lower()
    if again != "yes":
        print("GoodBye :)")
        break



