import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import os

class TranscribePage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=30)

        tb.Label(self, text="Transcribe Audio", font=("Helvetica", 24, "bold")).pack(pady=20)

        tb.Button(self, text="Upload MP3", bootstyle=PRIMARY, width=20, command=self.upload_file).pack(pady=10)
        tb.Button(self, text="Back to Dashboard", bootstyle=INFO,
                  command=lambda: master.show_screen("DashboardPage")).pack(pady=20)

        self.output_box = tb.ScrolledText(self, width=80, height=20, font=("Helvetica", 12))
        self.output_box.pack(pady=20)

    def upload_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if filepath:
            # 🔹 Placeholder: here you'd call your AI transcription function
            notes = f"✅ Processed file: {os.path.basename(filepath)}\n\n(Transcription + notes would appear here.)"
            self.output_box.delete(1.0, "end")
            self.output_box.insert("end", notes)
        else:
            messagebox.showwarning("No file", "Please select an audio file.")
