# request_page.py
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class RequestPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master)

        tb.Label(self, text="Post a Request", font=("Helvetica", 24, "bold")).pack(pady=20)

        form = tb.Frame(self)
        form.pack()

        tb.Label(form, text="Professor Name").pack(anchor="w")
        self.prof_entry = tb.Entry(form, width=35)  
        self.prof_entry.pack(anchor="w", pady=(0, 8))

        tb.Label(form, text="Class Number").pack(anchor="w")
        self.class_entry = tb.Entry(form, width=35)  
        self.class_entry.pack(anchor="w", pady=(0, 8))

        tb.Label(form, text="Room Number").pack(anchor="w")
        self.room_entry = tb.Entry(form, width=35)  
        self.room_entry.pack(anchor="w", pady=(0, 12))

        # Buttons: purple primary + purple outline (colors come from main.py styles)
        buttons = tb.Frame(self)
        buttons.pack(pady=10)

        tb.Button(
            buttons, text="Submit Request",
            bootstyle=PRIMARY,  # solid purple
            command=self.submit_request
        ).pack(side="left", padx=6)

        tb.Button(
            buttons, text="Back",
            bootstyle="primary-outline",  # purple outline
            command=lambda: master.show_screen("DashboardPage")
        ).pack(side="left", padx=6)

    def submit_request(self):
        request = {
            "professor": self.prof_entry.get(),
            "class_number": self.class_entry.get(),
            "room": self.room_entry.get()
        }
        self.master.requests.append(request)
        self.master.show_screen("DashboardPage")

