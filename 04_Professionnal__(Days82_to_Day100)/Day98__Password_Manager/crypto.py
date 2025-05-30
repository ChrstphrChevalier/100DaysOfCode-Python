from cryptography.fernet import Fernet
import os

KEY_FILE = os.path.join(os.path.dirname(__file__), ".secret.key")

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

def encrypt_data(data: str) -> str:
    key = load_key()            
    fernet = Fernet(key)        
    token = fernet.encrypt(data.encode())
    return token.decode()               

def decrypt_data(token: str) -> str:
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(token.encode())
    return decrypted.decode()               
