from tkinter import *

class BrowseRequestsPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Browse Requests", font=("Arial", 24)).pack(pady=20)

        self.listbox = Listbox(self, width=80, height=20)
        self.listbox.pack()

        Button(self, text="Back", command=lambda: master.show_screen("DashboardPage")).pack(pady=5)

    def tkraise(self, *args, **kwargs):
        """Refresh list when shown."""
        super().tkraise(*args, **kwargs)
        self.listbox.delete(0, END)
        for req in self.master.requests:
            self.listbox.insert(END, f"{req['professor']} - {req['class_number']} - {req['room']}")
