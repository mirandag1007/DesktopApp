from tkinter import *

class DashboardPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Dashboard", font=("Arial", 24)).pack(pady=20)

        Button(self, text="Record Lecture", command=lambda: master.show_screen("RecordingPage")).pack(pady=5)
        Button(self, text="View Transcriptions", command=lambda: master.show_screen("MarkdownViewerPage")).pack(pady=5)
        Button(self, text="Post Request", command=lambda: master.show_screen("RequestPage")).pack(pady=5)
        Button(self, text="Browse Requests", command=lambda: master.show_screen("BrowseRequestsPage")).pack(pady=5)
        Button(self, text="Logout", command=lambda: master.show_screen("LoginPage")).pack(pady=5)
