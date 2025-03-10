# Password Manager

Password Manager app is a standalone executable created using Python and packaged with PyInstaller.
It provides a user-friendly GUI for securely saving passwords in a CSV file stored in the data folder.

## Features

- Generate Secure Passwords - Create strong passwords with a single button click.
- Quick Search - Enter a website or app name and press Search to find the closest match in the stored credentials.
- View All Saved Passwords - Click View All Sites to open a separate window displaying all stored credentials.
    - Right-click a row to delete an entry.
    - Double-click a column to instantly copy its value to the clipboard.

## Getting Started

No installation is required! Simply download the executable file and run it.

### First Run (Windows)

1. Download `password-manager` from the (https://github.com/VitaliySysak/password-manager) section.
2. In the src/dist folder, locate the main.exe file. Run it and create a shortcut to place on your desktop.
3. After adding your first password, a passwords.csv file will be automatically created inside the data folder.

## Important Notes

Do not move the passwords.csv file!
If the file is missing, the program will automatically create a new one in the data folder.

## For developers 

If you want to modify program.
1. In main.py, set debug=True before modifying the code. Once you finish, remember to set debug=False.
2. Install package (pip install pyinstaller)
3. Move to src directory and execute 
(pyinstaller --onefile --noconsole --icon=logo.ico --upx-exclude python39.dll --exclude matplotlib --strip main.py)
in terminal
