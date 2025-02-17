from tkinter import *
from PIL import Image, ImageTk
from actions import Actions, window
from tkinter import ttk

def on_enter_pressed(event):
    """Function to call when Enter is pressed."""
    print("Enter key pressed! Entry content:", event.widget.get())

class Interface(Actions):
    def __init__(self, debug, EMAIL, PHONE_NUMBER):
        super().__init__(debug)

        self.path = "./" if debug else "../"
        self.primary = "#1F1F1F"
        self.secondary = "#FFFFFf"

        self.email = EMAIL
        self.phone_number = PHONE_NUMBER
            
        window.title("Password Manager")
        window.config(padx=200, pady=60, bg=self.primary)
        window.geometry("1280x720")
        window.minsize(920, 600)

    def create_gui(self):
        self.draw_images()
        self.create_labels()
        self.create_inputs()
        self.create_buttons()
        
    def draw_images(self):
        self.canvas = Canvas(width=400, height=380, bg=self.primary, highlightthickness=0)
        pil_image = Image.open(self.path + "logo.png")
        resized_image = pil_image.resize((300, 300)) 
        self.logo_img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(200, 200, image=self.logo_img)
        self.canvas.grid(row=0, column=1)
    
    def create_labels(self):
        self.website_or_app_label = Label(text="Website/App:", font=("Arial", 16, "bold"), bg=self.primary, fg=self.secondary)
        self.website_or_app_label.grid(row=1, column=0, padx=(56, 0))
        self.username_or_email_label = Label(text="Email/Username:", font=("Arial", 16, "bold"), bg=self.primary, fg=self.secondary)
        self.username_or_email_label.grid(row=2, column=0, padx=(56, 0))
        self.phone_number_label = Label(text="Phone number:", font=("Arial", 16, "bold"), bg=self.primary, fg=self.secondary)
        self.phone_number_label.grid(row=3, column=0, padx=(56, 0))
        self.password_label = Label(text="Password:", font=("Arial", 16, "bold"), bg=self.primary, fg=self.secondary)
        self.password_label.grid(row=4, column=0, padx=(56, 0))
    
    def create_inputs(self):
        self.website_or_app_input = Entry(
            width=31, font=("Arial", 15),
            bg=self.primary, fg=self.secondary,
            border=4, insertbackground=self.secondary
        )
        self.website_or_app_input.bind("<Return>", self.find_password)
        self.website_or_app_input.focus()
        self.website_or_app_input.grid(row=1, column=1, padx=(18, 0), pady=(0, 4))

        self.username_or_email_input = Entry(
            width=31, font=("Arial", 15),
            bg=self.primary, fg=self.secondary,
            border=4, insertbackground=self.secondary
        )
        self.username_or_email_input.insert(END, self.email)
        self.username_or_email_input.grid(row=2, column=1, padx=(18, 0), pady=(0, 4))

        self.phone_number_input = Entry(
            width=31, font=("Arial", 15),
            bg=self.primary, fg=self.secondary,
            border=4, insertbackground=self.secondary
        )
        self.phone_number_input.insert(END, self.phone_number)
        self.phone_number_input.grid(row=3, column=1, padx=(18, 0), pady=(0, 4))

        self.password_input = Entry(
            width=31, font=("Arial", 15),
            bg=self.primary, fg=self.secondary,
            border=4, insertbackground=self.secondary
        )
        self.password_input.grid(row=4, column=1, padx=(18, 0), pady=(0, 5))

    def create_buttons(self):
        self.search_button = Button(
            text="Search",
            width=22,
            font=("Arial", 11, "bold"),
            command=self.find_password,
            bg=self.primary,
            fg=self.secondary,
            border=2,
            activebackground="#303030",
            activeforeground=self.secondary
        )
        self.search_button.grid(row=1, column=2, sticky="E", padx=(0, 92), pady=(0, 4))

        self.all_sites_button = Button(
            text="View All Sites",
            width=22,
            font=("Arial", 11, "bold"),
            command=self.show_all_sites,
            bg=self.primary,
            fg=self.secondary,
            border=2,
            activebackground="#303030",
            activeforeground=self.secondary
        )
        self.all_sites_button.grid(row=2, column=2, sticky="E", padx=(0, 92), pady=(0, 4))

        self.copy_phone_button = Button(
            text="Copy number",
            width=22,
            font=("Arial", 11, "bold"),
            command=self.copy_phone_number,
            bg=self.primary,
            fg=self.secondary,
            border=2,
            activebackground="#303030",
            activeforeground=self.secondary
        )
        self.copy_phone_button.grid(row=3, column=2, sticky="E", padx=(0, 92), pady=(0, 4))

        self.password_button = Button(
            text="Generate Password",
            width=22,
            font=("Arial", 11, "bold"),
            command=self.generate_password,
            bg=self.primary,
            fg=self.secondary,
            border=2,
            activebackground="#303030",
            activeforeground=self.secondary
        )
        self.password_button.grid(row=4, column=2, sticky="E", padx=(0, 92), pady=(0, 4))

        self.add_button = Button(
            text="Add",
            width=47,
            font=("Arial", 14, "bold"),
            command=self.add_data,
            bg=self.primary,
            fg=self.secondary,
            border=2,
            activebackground="#303030",
            activeforeground=self.secondary
        )
        self.add_button.grid(row=5, column=1, columnspan=2, sticky="E", padx=(0, 92))

    def message_box(self, *args, title, popup_type="warning", offset_y=-10, height=140):
        popup = Toplevel(window)
        popup.title(title)
        popup.configure(bg=self.primary)
        popup.transient(window) 
        popup.resizable(False, False)
        popup.bind("<Return>", lambda _: popup.destroy())
        popup.focus_set()

        if popup_type == "info":
            icon = "ℹ"
            bg_color = "#3498db" 
        elif popup_type == "warning":
            icon = "⚠️"
            bg_color = "#e67e22"
        else:
            icon = "❗"
            bg_color = "#c0392b" 

        header = Frame(popup, bg=bg_color, height=30)
        header.pack(fill="x")
            
        header_label = Label(header, text=f" {icon} {title}", font=("Arial", 14, "bold"), fg="white", bg=bg_color)
        header_label.pack(pady=6, padx=10)

        for message in args:
            if len(message) > 4:
                height += 4
            if len(message) > 25 and popup_type != "info" and popup_type != "warning":
                height += 30
                
            if len(message) > 35:
                height += 20
            label = Label(popup, text=message, font=("Consolas", 13, "bold"), bg=self.primary, fg=self.secondary, wraplength=350)
            label.pack(anchor="w", padx=20) if popup_type == "info" else label.pack(pady=6)

        popup.geometry(f"380x{height}")

        self.center_window(popup, window_width=380, window_height=height)
            
        close_button_frame = Frame(popup, bg="#252525", height=60)
        close_button_frame.pack(fill="x", side="bottom")
        
        close_button = Button(
                        popup, text="OK",
                        command=popup.destroy,
                        font=("Arial", 12, "bold"),
                        bg="#303030", 
                        fg=self.secondary, 
                        activebackground="#303030",
                        activeforeground=self.secondary, 
                        relief="solid",
                        borderwidth=0, 
                        highlightthickness=0
                    )  
        
        close_button.place(x=270, y=height - 44, width=80, height=25)
        
    def show_all_sites(self):
        popup = Toplevel(window)
        popup.title("All Sites")
        popup.geometry("1280x720")
        popup.config(bg=self.primary)
        popup.minsize(920, 600)
        
        self.center_window(popup)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            font=("Helvetica", 16),
            rowheight=30,
            background=self.primary,
            foreground=self.secondary,
            fieldbackground=self.primary
        ) 

        style.configure("Vertical.TScrollbar",
            bordercolor="#424242",  
            arrowcolor="#424242",   
            relief="flat",      
            gripcount=0,        
            lightcolor="#424242",  
            darkcolor="#424242"
        ) 
        style.map("Vertical.TScrollbar",
            background=[("active", "#434343"), ("!active", "#424242")],  
            troughcolor=[("active", self.primary), ("!active", self.primary)],
            arrowcolor=[("active", "white"), ("!active", "white")]
        )

        style.configure("Treeview.Heading",
            font=("Helvetica", 18, "bold"),
            background=self.primary,
            foreground=self.secondary,
            borderwidth=0,
            padx=5,        
            pady=5       
        )
        style.map("Treeview.Heading",
            background=[("active", "#4A6984"), ("!active", self.primary)],
            foreground=[("active", self.secondary), ("!active", self.secondary)]
        )
        
        frame = Frame(popup, bg=self.primary)
        frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame, selectmode="browse", show="headings")

        self.fill_data_rows(self.tree, popup)

        self.tree.bind("<Double-1>", self.on_item_double_click)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview, style="Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree.pack(side="left", fill="both", expand=True) 

        self.context_menu = Menu(self.tree, tearoff=0)
        self.context_menu.add_command(label="Delete Row", command=self.delete_selected_row)

        self.tree.bind("<Button-3>", self.show_context_menu)  
    
    def show_context_menu(self, event):
        selected_item = self.tree.identify_row(event.y) 
        if selected_item:  
            self.tree.selection_set(selected_item) 
            self.context_menu.post(event.x_root, event.y_root)