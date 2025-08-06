from tkinter import *
from login import LoginPage

# Creating class for main app window 
class App(Tk):
    def __init__(self):
        # Intializing parent Tk class
        super().__init__()

        # Setting title and  size for app window
        self.title("Relay")
        self.state("zoomed")

        # Creating dictionary to store all screen frames
        self.frames = {}

        # Loop to load screen classes
        for ScreenClass in (LoginPage, ):                       # added ',' to add future screens
            screen = ScreenClass(self)                          # Create instance of screen
            self.frames[ScreenClass.__name__] = screen          # Store screen object in dictionary with class name as key
            screen.grid(row = 0, column = 0, sticky = "nsew")   # Place screen widget in main window using grid layout (nsew makes it fill entire window)

        # Show the login page as the main screen when app is started
        self.show_screen("LoginPage")

    # Function to bring a screen to the front based on name
    def show_screen(self, name):
        screen = self.frames[name] # Look for screen in dictionary
        screen.tkraise() # Make selected screen visible

if __name__ == "__main__":
    app = App()
    app.mainloop()