import os
import string
from interface import Interface
from settings import window

class PasswordManager(Interface):
    def __init__(self, debug):
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.APP_WIDTH = 880
        self.APP_HEIGHT = 700
        self.path = "./" if debug else "../"
        self.data_path = '../' if debug else '../../'
        os.makedirs(self.data_path + "data", exist_ok=True)
        super().__init__()

        window.title("Password Manager")
        window.config(padx=200, pady=60, bg=self.primary)
        window.minsize(920, 600)

        self.lower_letters = list(string.ascii_lowercase)
        self.upper_letters = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_offset = (screen_width - self.WINDOW_WIDTH) // 2
        y_offset = (screen_height - self.WINDOW_HEIGHT) // 2

        window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x_offset}+{y_offset -40}")

        self.create_gui()

if __name__ == "__main__":
    password_manager = PasswordManager(debug=False)
    window.mainloop()