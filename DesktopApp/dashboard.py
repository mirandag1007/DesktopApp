import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

class DashboardPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master)


        Button(self, text="Record Lecture", command=lambda: master.show_screen("RecordingPage")).pack(pady=5)
        Button(self, text="View Transcriptions", command=lambda: master.show_screen("MarkdownViewerPage")).pack(pady=5)
        Button(self, text="Post Request", command=lambda: master.show_screen("RequestPage")).pack(pady=5)
        Button(self, text="Browse Requests", command=lambda: master.show_screen("BrowseRequestsPage")).pack(pady=5)
        Button(self, text="Logout", command=lambda: master.show_screen("LoginPage")).pack(pady=5)
        Button(self, text="Transcribe Audio", command=lambda: master.show_screen("TranscribePage")).pack(pady=5)

        # helper to navigate between screens
        def go(screen_name: str):
            if hasattr(master, "frames") and screen_name in master.frames:
                master.show_screen(screen_name)
            else:
                messagebox.showinfo("Coming soon", f"{screen_name} is not implemented yet.")

        # helper to get the real background color of a ttkbootstrap card
        def get_card_bg():
            return master.style.lookup("secondary.TFrame", "background") or "#2f3339"

        card_bg = get_card_bg()

        
        nav = tb.Frame(self)
        nav.pack(side="top", fill="x", pady=(8, 4), padx=12)

        nav_right = tb.Frame(nav)
        nav_right.pack(side="right")

        tb.Button(nav_right, text="Dashboard", bootstyle="primary-outline",
                  command=lambda: go("DashboardPage")).pack(side="left", padx=(0, 8))
        tb.Button(nav_right, text="Connect", bootstyle="primary-outline",
                  command=lambda: go("ConnectPage")).pack(side="left", padx=(0, 8))
        tb.Button(nav_right, text="Logout", bootstyle="primary-outline",
                  command=lambda: go("LoginPage")).pack(side="left")

        
        tb.Label(self, text="Dashboard", font=("Helvetica", 24, "bold")).pack(
            anchor="w", padx=20, pady=(10, 20)
        )

        
        notes_frame = tb.Frame(self, padding=20, bootstyle="secondary")
        notes_frame.pack(fill="x", padx=20, pady=(0, 30))

        tk.Label(notes_frame, text="Your Notes",
                 font=("Helvetica", 14, "bold"),
                 fg="#FFFFFF", bg=card_bg).pack(anchor="w")
        tk.Label(notes_frame, text="Saved lecture transcriptions",
                 fg="#94A3B8", bg=card_bg).pack(anchor="w")

        tb.Button(notes_frame, text="+ Transcribe a Note",
                  bootstyle=PRIMARY, width=22,
                  command=lambda: master.show_screen("RecordingPage")).pack(anchor="e", pady=(10, 0))

        
        connect_header = tb.Frame(self)
        connect_header.pack(fill="x", padx=20)
        tb.Label(connect_header, text="Connect", font=("Helvetica", 16, "bold")).pack(anchor="w")
        tb.Label(connect_header, text="Find other students or request help",
                 bootstyle="secondary").pack(anchor="w", pady=(0, 10))

        
        cards = tb.Frame(self)
        cards.pack(fill="x", padx=20, pady=(0, 20))

        # Browse Requests card
        browse_card = tb.Frame(cards, padding=20, bootstyle="secondary")
        browse_card.pack(side="left", expand=True, fill="x", padx=(0, 10))

        tk.Label(browse_card, text="Browse Requests",
                 font=("Helvetica", 14, "bold"),
                 fg="#FFFFFF", bg=card_bg).pack(anchor="w")
        tk.Label(browse_card, text="Find students who need note-taking help",
                 fg="#94A3B8", bg=card_bg).pack(anchor="w", pady=(4, 10))
        tb.Button(browse_card, text="Open", bootstyle=PRIMARY,
                  command=lambda: master.show_screen("BrowseRequestsPage")).pack(anchor="e")

        # Make a Request card
        request_card = tb.Frame(cards, padding=20, bootstyle="secondary")
        request_card.pack(side="left", expand=True, fill="x", padx=(10, 0))

        tk.Label(request_card, text="Make a Request",
                 font=("Helvetica", 14, "bold"),
                 fg="#FFFFFF", bg=card_bg).pack(anchor="w")
        tk.Label(request_card, text="Request notes from your classmates",
                 fg="#94A3B8", bg=card_bg).pack(anchor="w", pady=(4, 10))
        tb.Button(request_card, text="Create", bootstyle=PRIMARY,
                  command=lambda: master.show_screen("RequestPage")).pack(anchor="e")

