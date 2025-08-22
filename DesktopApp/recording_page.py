import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sounddevice as sd
import wavio
import os

class RecordingPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=30)

        tb.Label(self, text="Record Audio", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.recording = None
        self.fs = 44100  # sample rate

        tb.Button(self, text="Start Recording", bootstyle=SUCCESS, width=20, command=self.start_recording).pack(pady=10)
        tb.Button(self, text="Stop Recording", bootstyle=DANGER, width=20, command=self.stop_recording).pack(pady=10)

        tb.Button(self, text="Back to Dashboard", bootstyle=INFO,
                  command=lambda: master.show_screen("DashboardPage")).pack(pady=20)

    def start_recording(self):
        duration = 10  # seconds, you can adjust or make it user input
        self.recording = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        os.makedirs("recordings", exist_ok=True)
        wavio.write("recordings/recorded_audio.wav", self.recording, self.fs, sampwidth=2)

    def stop_recording(self):
        # Stop recording early (not strictly needed if fixed duration)
        sd.stop()
