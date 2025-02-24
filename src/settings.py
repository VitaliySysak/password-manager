from tkinter import *
import json

window = Tk()

class Settings:
    def __init__(self):
        self.secret_key = self.load_key()
        window.bind("<Configure>", self.on_configure)
    
    def get_settings(self):
        try:
            with open(self.path + "settings.json", "r") as settings:
                settings_data = json.load(settings)
        except FileNotFoundError:
            email = ""
            phone_number = ""
            is_maximize_on = False

            settings_data = {
                "email": email,
                "phone_number": phone_number,
                "maximize_window": is_maximize_on
            }

            with open(self.path + "settings.json", "w") as settings:
                json.dump(settings_data, settings, indent=4)
    
        self.email = settings_data["email"]
        self.phone_number = settings_data["phone_number"]

        self.is_maximize_on = BooleanVar(value=bool(self.get_setting_value()))
        
        if self.get_setting_value():
            window.state("zoomed")

    def apply_settings(self, popup):
        email = self.settings_email_input.get().lower()
        phone_number = self.settings_phone_number_input.get().lower()
        is_maximize_on = self.is_maximize_on.get()
        secret_key = self.settings_secret_key_input.get()

        with open(self.path + "secret.key", "wb") as key_file:
                key_file.write(secret_key.encode("utf-8"))
        
        self.secret_key = secret_key
        
        settings_data = {
            "email": email,
            "phone_number": phone_number,
            "maximize_window": is_maximize_on
        }

        with open(self.path + "settings.json", "w") as settings:
            json.dump(settings_data, settings, indent=4)

        self.username_or_email_input.delete(0, END)
        self.phone_number_input.delete(0, END)

        self.username_or_email_input.insert(END, email)
        self.phone_number_input.insert(END, phone_number)

        if is_maximize_on:
            window.state("zoomed")
        else:
            window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
            window.state("normal")

        self.get_settings()
        popup.destroy()

    def get_setting_value(self):
        with open(self.path + "settings.json") as settings:
            settings_data = json.load(settings)
        
        return settings_data["maximize_window"]
    
    def toggle(self, value, button_on, button_off):
        self.is_maximize_on.set(value)
        if value:
            button_on.config(state="disabled", relief="sunken")
            button_off.config(state="normal", relief="raised")
        else:
            button_on.config(state="normal", relief="raised")
            button_off.config(state="disabled", relief="sunken")
    
    def on_configure(self, _):
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        x_offset = (window_width - self.APP_WIDTH) // 2
        y_offset = (window_height - self.APP_HEIGHT) // 2

        self.settings_button.place(x=self.APP_WIDTH + x_offset - 70, y=-y_offset)

        window.config(padx=x_offset, pady=y_offset, bg=self.primary)