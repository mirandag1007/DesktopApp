import ttkbootstrap as tb
from ttkbootstrap.constants import *

class LoginPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=30)

        tb.Label(self, text="Relay Login", font=("Helvetica", 32, "bold"), bootstyle=PRIMARY).pack(pady=30)

        tb.Label(self, text="Username", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.username_entry = tb.Entry(self, width=35, font=("Helvetica", 14))
        self.username_entry.pack()

        tb.Label(self, text="Password", font=("Helvetica", 16)).pack(pady=(10, 5))
        self.password_entry = tb.Entry(self, show="*", width=35, font=("Helvetica", 14))
        self.password_entry.pack()

        tb.Button(self, text="Login", bootstyle=SUCCESS, width=25, command=self.login).pack(pady=20)
        tb.Button(self, text="Go to Dashboard", bootstyle=INFO, width=25,
                  command=lambda: master.show_screen("DashboardPage")).pack()

    def login(self):
        username = self.username_entry.get()
        self.master.current_user = username
        self.master.show_screen("DashboardPage")
