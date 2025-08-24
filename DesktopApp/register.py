import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from auth import register_user

class RegisterPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=30)

        container = tb.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tb.Label(container, text="Create Account", font=("Helvetica", 28, "bold"), style="Heading.TLabel").pack(pady=20)

        tb.Label(container, text="Username", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.username_entry = tb.Entry(container, width=35, font=("Helvetica", 14))
        self.username_entry.pack()

        tb.Label(container, text="Password", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.password_entry = tb.Entry(container, show="*", width=35, font=("Helvetica", 14))
        self.password_entry.pack()

        tb.Button(container, text="Register", bootstyle=SUCCESS, width=25, command=self.register).pack(pady=20)
        tb.Button(container, text="Back to Login", bootstyle=INFO, width=25, command=lambda: master.show_screen("LoginPage")).pack()

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            Messagebox.show_warning("Please enter both username and password.", "Missing Information")
            return

        if register_user(username, password):
            Messagebox.show_info("Account created successfully!", "Success")
            self.master.show_screen("LoginPage")
        else:
            Messagebox.show_error("Username already exists. Please choose another.", "Registration Failed")


