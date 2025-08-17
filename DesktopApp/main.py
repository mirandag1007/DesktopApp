import ttkbootstrap as tb
from ttkbootstrap.constants import *
from login import LoginPage
from dashboard import DashboardPage
from markdown_viewer import MarkdownViewerPage
from request_page import RequestPage
from browse_request import BrowseRequestsPage

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="cosmo")  # Try: cosmo, darkly, journal, lumen
        self.title("Relay")
        self.state("zoomed")

        

        # Shared data
        self.current_user = None
        self.transcriptions = []
        self.requests = []

        #just for style 
        self.style.configure('.', font=('Helvetica', 14))
        self.option_add("*TButton.Padding", 10)
        self.option_add("*TEntry.Font", ("Helvetica", 14))

        self.frames = {}
        for ScreenClass in (
            LoginPage,
            DashboardPage,          
            MarkdownViewerPage,
            RequestPage,
            BrowseRequestsPage
        ):
            screen = ScreenClass(self)
            self.frames[ScreenClass.__name__] = screen
            screen.grid(row=0, column=0, sticky="nsew")

        self.show_screen("LoginPage")

    def show_screen(self, name):
        self.frames[name].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()