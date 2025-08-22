# browse_request.py
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class BrowseRequestsPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master)

        tb.Label(self, text="Browse Requests", font=("Helvetica", 24, "bold")).pack(pady=20)

        # List of requests (tk Listbox is fine alongside ttkbootstrap)
        self.listbox = tk.Listbox(self, width=80, height=20)
        self.listbox.pack()

        # Buttons: make them purple to match your theme
        btns = tb.Frame(self)
        btns.pack(pady=10)

        tb.Button(btns, text="Back",
                  bootstyle="primary-outline",
                  command=lambda: master.show_screen("DashboardPage")).pack(side="left", padx=6)

        tb.Button(btns, text="Open Selected", bootstyle=PRIMARY,
                  command=self.open_selected).pack(side="left", padx=6)

    def tkraise(self, *args, **kwargs):
        """Refresh list when shown."""
        super().tkraise(*args, **kwargs)
        self.listbox.delete(0, tk.END)
        for req in self.master.requests:
            self.listbox.insert(tk.END, f"{req['professor']} - {req['class_number']} - {req['room']}")

    def open_selected(self):
        idx = self.listbox.curselection()
        if idx:
            # handle selection
            pass
