from tkinter import *
import pyperclip
import pandas as pd
from settings import Settings
from password import Crypto
import cryptography.fernet

class Actions(Settings, Crypto):
    def __init__(self):
        super().__init__()

    def add_data(self):
        website_or_app = self.website_or_app_input.get().lower()
        username_or_email = self.username_or_email_input.get()
        phone_number = self.phone_number_input.get()
        password = self.password_input.get()

        decrypted_password= self.encrypt_password(password=password)
        
        row = {
            "Website/App": website_or_app,
            "Email/Username": username_or_email,
            "Phone number": phone_number,
            "Password": decrypted_password
        }

        if not website_or_app or not username_or_email or not phone_number or not password:
            self.message_box("Please don't leave any fields empty!", title="Warning", popup_type="warning", height=120)
        else:
            try:
                self.df = pd.read_csv(self.data_path + 'data/passwords.csv', index_col=0, dtype={"Phone number": str})
                self.df.index = range(1, len(self.df) + 1)
                if not self.df[self.df["Website/App"] == website_or_app].empty:
                    self.message_box(f"Info about \"{website_or_app.capitalize()}\" already exist", title="Warning", popup_type="warning")
                    return 
                new_row = pd.DataFrame([row])

                self.df = pd.concat([self.df, new_row], ignore_index=True)

            except FileNotFoundError:
                columns = ["Website/App", "Email/Username", "Phone number", "Password"]
                self.df = pd.DataFrame([row], columns=columns)

            self.df["Phone number"] = self.df["Phone number"].astype(str)
            self.df.index = range(1, len(self.df) + 1)
            self.df.to_csv(self.data_path + 'data/passwords.csv', index=True, index_label="ID")

            self.website_or_app_input.delete(0, END)
            self.password_input.delete(0, END)

    def find_password(self, _=None):
        website_found = False
        try:
            self.df = pd.read_csv(self.data_path + "data/passwords.csv", dtype={"Phone number": str})

            website = self.website_or_app_input.get().lower()
            username_or_email = self.username_or_email_input.get().lower()

            if website == "":
                self.message_box("Website input is empty!", title="Warning", popup_type="warning")

                return
        except FileNotFoundError:
            self.message_box("No sites found", title="Error", popup_type="error")

            return
        for _, row in self.df.iterrows():
            if website in row["Website/App"] and username_or_email in row["Email/Username"]:
                
                match_website = row["Website/App"]
                match_email = row["Email/Username"]
                match_password = row["Password"]

                website_found = True 

                if website == match_website:
                    break
                
        if not website_found:
            self.message_box(
                f"No details about website \"{website.capitalize()}\" exists",
                title="Warning",
                popup_type="warning",
                height=120
            )
        else:
            self.username_or_email_input.delete(0, END)
            self.username_or_email_input.insert(END, match_email)
            try:
                password = self.decrypt_password(match_password)
                pyperclip.copy(password)
                self.password_input.delete(0, END)
                self.password_input.insert(END, password)
                self.password_input.config(show="*")

                self.message_box(
                    f"   Website/App: {match_website.capitalize()}",
                    f"Email/Username: {match_email}",
                    f"      Password: {"*" * len(password)}",
                    title="Info",
                    popup_type="info",
                    height=180,
                )
            except cryptography.fernet.InvalidToken:
                self.message_box("Invalid secret key!", title="Error", popup_type="error")
            except ValueError:
                self.message_box("Invalid secret key!", title="Error", popup_type="error")
            
    def fill_data_rows(self, tree, popup):
        self.popup = popup
        self.tree = tree
        try:
            self.df = pd.read_csv(self.data_path + 'data/passwords.csv', dtype={"Phone number": str})
        except FileNotFoundError:
            columns = ["Website/App", "Email/Username", "Phone number", "Password"]

            self.df = pd.DataFrame(columns=columns)
            self.df["Phone number"] = self.df["Phone number"].astype(str)
            
            self.df.index = range(1, len(self.df) + 1)
            self.df.to_csv(self.data_path + 'data/passwords.csv', index=True, index_label="ID")

            self.df = pd.read_csv(self.data_path + 'data/passwords.csv', dtype={"Phone number": str})

        tree["columns"] = list(self.df.columns)

        for col in self.df.columns:
            tree.heading(col, text=col)
            if col == "ID":
                tree.column(col, width=50, anchor="center", stretch=False)
            elif col == "Website/App":
                tree.column(col, width=350, anchor="w")
            elif col == "Email/Username":
                tree.column(col, width=100, anchor="w")
            elif col == "Phone number":
                tree.column(col, width=80, anchor="w")
            elif col == "Password":
                tree.column(col, width=120, anchor="w")

        for _, row in self.df.iterrows(): 
            row_values = list(row)
            row_values[-1] = "*" * 30
            tree.insert("", "end", values=row_values)

    def copy_phone_number(self):
        phone_number = self.phone_number_input.get()[3:] if "+38" in self.phone_number_input.get() else self.phone_number_input.get()
        pyperclip.copy(phone_number)

    def on_item_double_click(self, event):
        try:
            selected_item = self.tree.selection()
            if selected_item:
                item_values = self.tree.item(selected_item)["values"]
                col_id = self.tree.identify_column(event.x)
                column_name = self.tree.heading(col_id)["text"]
                
                if column_name in self.df.columns:
                    column_index = self.df.columns.get_loc(column_name)
                    if column_index < len(item_values):
                        if column_name == "Phone number":
                            if "+38" in "+" + str(item_values[column_index]):
                                cell_value = str(item_values[column_index])[2:]
                            else:
                                cell_value = "0" + str(item_values[column_index])
                            text = f"Copied: {cell_value}"
                        elif column_name == "Password":
                            encrypted_password = self.df.iloc[item_values[0] - 1, 4]
                            cell_value = self.decrypt_password(encrypted_password)
                            text = "Pasword copied to clipboard"
                        else:
                            cell_value = str(item_values[column_index])
                            text = f"Copied: {cell_value}"

                        pyperclip.copy(cell_value)

                        if hasattr(self, "copied_label") and self.copied_label.winfo_exists():
                            self.copied_label.destroy()

                        self.copied_label = Label(self.popup, text=text, font=("Helvetica", 18), fg="green", bg=self.primary)
                        self.copied_label.pack()
        except cryptography.fernet.InvalidToken:
            self.message_box("Invalid secret key!", title="Error", popup_type="error")
        except ValueError:
            self.message_box("Invalid secret key!", title="Error", popup_type="error")

    def center_window(self, window, window_width=1280, window_height=720):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        x_offset = (screen_width - window_width) // 2
        y_offset = (screen_height - window_height) // 2
        window.geometry(f'{window_width}x{window_height}+{x_offset}+{y_offset}')

    def delete_selected_row(self, popup):
        selected_item = self.tree.selection()
        if selected_item:
            row_id = self.tree.item(selected_item, "values")[0]
            self.df = self.df[self.df["ID"] != int(row_id)]
            self.df.reset_index(drop=True, inplace=True)
            self.df["ID"] = range(1, len(self.df) + 1) 
            self.df.to_csv(self.data_path + "data/passwords.csv", index=False)
            
            self.tree.delete(selected_item) 

        self.tree.delete(*self.tree.get_children())
        self.fill_data_rows(self.tree, popup)

