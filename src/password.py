from cryptography.fernet import Fernet
from random import choice, randint, shuffle
from tkinter import *

class Crypto:
    def generate_password(self):
        password_lower_letters = [choice(self.lower_letters) for _ in range(randint(4, 6))]
        password_upper_letters = [choice(self.upper_letters) for _ in range(randint(4, 6))]
        password_numbers = [choice(self.numbers) for _ in range(randint(4, 6))]
        password_symbols = [choice(self.symbols) for _ in range(randint(4, 6))]

        password_list = password_upper_letters + password_lower_letters + password_numbers + password_symbols
        shuffle(password_list)

        password = "".join(password_list)
        self.password_input.delete(0, END)
        self.password_input.config(show="")
        self.password_input.insert(END, password)

    def load_key(self):
        try:
            with open(self.path + "secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.path + "secret.key", "wb") as key_file:
                key_file.write(key)
                return key

    def decrypt_password(self, password: str):
        cipher = Fernet(self.secret_key)
        decrypted_password = cipher.decrypt(password).decode()

        return decrypted_password
    
    def encrypt_password(self, password: str):
        cipher = Fernet(self.secret_key)
        encrypted_password = cipher.encrypt(password.encode())
        
        return encrypted_password.decode()