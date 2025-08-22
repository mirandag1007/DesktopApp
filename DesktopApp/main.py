import ttkbootstrap as tb
from ttkbootstrap.constants import *
from login import LoginPage
from dashboard import DashboardPage
from markdown_viewer import MarkdownViewerPage
from request_page import RequestPage
from browse_request import BrowseRequestsPage
from register import RegisterPage

# Accent colors for buttons/text
ACCENT_PURPLE = "#6C5CE7"
ACCENT_PURPLE_ACTIVE = "#7567EA"
ACCENT_PURPLE_PRESSED = "#5B4FE0"
TEXT_MAIN = "#E5E7EB"
TEXT_MUTED = "#94A3B8"

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly") # Using ttkbootstrap's dark theme for UI

        self.title("Relay")
        self.state("zoomed")

        # Let the window’s grid expand fully
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # App State
        self.current_user = None
        self.transcriptions = []
        self.requests = []

        # Text Styling
        style = self.style
        style.configure(".", font=("Helvetica", 14))
        style.configure("TLabel", foreground=TEXT_MAIN)
        style.configure("Muted.TLabel", foreground=TEXT_MUTED)
        style.configure("Heading.TLabel", font=("Helvetica", 32, "bold"))
        style.configure("Subheading.TLabel", font=("Helvetica", 20, "bold"))

        self.option_add("*TButton.Padding", 12)
        self.option_add("*TEntry.Font", ("Helvetica", 14))

        # Button styles
        style.configure("Primary.TButton", background=ACCENT_PURPLE, foreground="white", font=("Helvetica", 12, "bold"))
        style.map("Primary.TButton", background=[("active", ACCENT_PURPLE_ACTIVE), ("pressed", ACCENT_PURPLE_PRESSED)])

        style.configure("primary.Outline.TButton", foreground=ACCENT_PURPLE, font=("Helvetica", 12))
        style.map("primary.Outline.TButton", foreground=[("active", ACCENT_PURPLE_ACTIVE)])

        self.frames = {}
        for ScreenClass in (
            LoginPage,
            DashboardPage,
            RegisterPage,
            MarkdownViewerPage,
            RequestPage,
            BrowseRequestsPage
        ):
            screen = ScreenClass(self)
            self.frames[ScreenClass.__name__] = screen
            screen.grid(row=0, column=0, sticky="nsew") # Put every screen in the same cell

        # Start on the login page
        self.show_screen("LoginPage")

    def show_screen(self, name):
        self.frames[name].tkraise() # Raise selected screen to the top


if __name__ == "__main__":
    app = App()
    app.mainloop()
