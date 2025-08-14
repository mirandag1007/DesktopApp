from tkinter import *
from tkinter import filedialog

class MarkdownViewerPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Markdown Viewer", font=("Arial", 24)).pack(pady=20)

        self.text_area = Text(self, width=80, height=25)
        self.text_area.pack()

        Button(self, text="Download as .md", command=self.download_file).pack(pady=5)
        Button(self, text="Back to Dashboard", command=lambda: master.show_screen("DashboardPage")).pack(pady=5)

    def tkraise(self, *args, **kwargs):
        """Refresh content when page is shown."""
        super().tkraise(*args, **kwargs)
        self.text_area.delete("1.0", END)
        if self.master.transcriptions:
            self.text_area.insert("1.0", self.master.transcriptions[-1])

    def download_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", END))
