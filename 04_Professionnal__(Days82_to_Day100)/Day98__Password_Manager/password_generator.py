import secrets
import string

def generate_password(length=16):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    while True:
        password = ''.join(secrets.choice(all_chars) for _ in range(length))

        has_letter = any(c in letters for c in password)
        has_digit = any(c in digits for c in password)
        has_symbol = any(c in symbols for c in password)

        if has_letter and has_digit and has_symbol:
            return password
