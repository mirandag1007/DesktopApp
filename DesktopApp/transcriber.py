from tkinter import *

class RequestPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Post a Request", font=("Arial", 24)).pack(pady=20)

        Label(self, text="Professor Name").pack()
        self.prof_entry = Entry(self)
        self.prof_entry.pack()

        Label(self, text="Class Number").pack()
        self.class_entry = Entry(self)
        self.class_entry.pack()

        Label(self, text="Room Number").pack()
        self.room_entry = Entry(self)
        self.room_entry.pack()

        Button(self, text="Submit Request", command=self.submit_request).pack(pady=10)
        Button(self, text="Back", command=lambda: master.show_screen("DashboardPage")).pack()

    def submit_request(self):
        request = {
            "professor": self.prof_entry.get(),
            "class_number": self.class_entry.get(),
            "room": self.room_entry.get()
        }
        self.master.requests.append(request)
        self.master.show_screen("DashboardPage")
