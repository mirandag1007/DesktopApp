import ttkbootstrap as tb
from ttkbootstrap.constants import *


from ttkbootstrap.dialogs import Messagebox
from auth import authorize

class LoginPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=30)


        container = tb.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tb.Label(container, text="Relay Login", font=("Helvetica", 32, "bold"), bootstyle=PRIMARY).pack(pady=30)

        tb.Label(container, text="Username", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.username_entry = tb.Entry(container, width=35, font=("Helvetica", 14))
        self.username_entry.pack()

        tb.Label(container, text="Password", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.password_entry = tb.Entry(container, show="*", width=35, font=("Helvetica", 14))
        self.password_entry.pack()

        tb.Button(container, text="Login", bootstyle=SUCCESS, width=25, command=self.login).pack(pady=20)
        tb.Button(container, text="Create Account", bootstyle=INFO, width=25,
                  command=lambda: master.show_screen("RegisterPage")).pack()

        # Make sure this page fills the window’s grid cell
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Centered container for the login form
        container = tb.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tb.Label(container, text="Relay Login", style="Heading.TLabel").pack(pady=(0, 24))

        # Username
        tb.Label(container, text="Username", style="Muted.TLabel", font=("Helvetica", 12)).pack(anchor="w")
        self.username_entry = tb.Entry(container, width=35)
        self.username_entry.pack(pady=(4, 12), fill="x")

        # Password
        tb.Label(container, text="Password", style="Muted.TLabel", font=("Helvetica", 12)).pack(anchor="w")
        self.password_entry = tb.Entry(container, show="*", width=35)
        self.password_entry.pack(pady=(4, 18), fill="x")

        # Buttons
        tb.Button(container, text="Login", bootstyle="Primary.TButton", width=25, command=self.login).pack(pady=(0, 10), fill="x")
        tb.Button(container, text="Create Account", bootstyle="primary-outline", width=25, command=lambda: master.show_screen("RegisterPage")).pack(fill="x")


    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if authorize(username, password):
            self.master.current_user = username
            self.master.show_screen("DashboardPage")
        else:

            tb.Messagebox.show_error("Invalid username or password", "Login Failed")

            Messagebox.show_error("Invalid username or password", "Login Failed")

