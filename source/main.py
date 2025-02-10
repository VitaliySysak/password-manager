from tkinter import *
import string
from interface import Interface
from actions import window
import os
from dotenv import load_dotenv

class PasswordManager(Interface):
    def __init__(self, debug):
        load_dotenv()
        super().__init__(debug, os.getenv("EMAIL"), os.getenv("PHONE_NUMBER"))
        self.lower_letters = list(string.ascii_lowercase)
        self.upper_letters = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 1280
        window_height = 720

        x_offset = (screen_width - window_width) // 2
        y_offset = (screen_height - window_height) // 2

        window.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset -40}")

        self.create_gui()

if __name__ == "__main__":
    password_manager = PasswordManager(debug=False)
    window.mainloop()