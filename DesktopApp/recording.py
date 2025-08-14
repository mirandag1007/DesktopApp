from tkinter import *
import sounddevice as sd
from scipy.io.wavfile import write
import requests
import tempfile
import os
import threading

ASSEMBLYAI_API_KEY = "YOUR_ASSEMBLYAI_API_KEY"  # replace with your key
SAMPLE_RATE = 44100  # Hz
RECORD_SECONDS = 500  # for testing; increase later

class RecordingPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="Recording Page", font=("Arial", 24)).pack(pady=20)

        self.status_label = Label(self, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        Button(self, text="Start Recording", command=self.start_recording).pack(pady=5)
        Button(self, text="Back to Dashboard", command=lambda: master.show_screen("DashboardPage")).pack(pady=5)

    def start_recording(self):
        """Start audio recording in a separate thread so UI stays responsive."""
        self.status_label.config(text="Recording...")
        threading.Thread(target=self.record_audio).start()

    def record_audio(self):
        try:
            audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished

            # Save temp WAV file
            temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            write(temp_wav.name, SAMPLE_RATE, audio)

            self.status_label.config(text="Uploading to AssemblyAI...")
            transcription_text = self.transcribe_audio(temp_wav.name)

            if transcription_text:
                self.master.transcriptions.append(transcription_text)
                self.status_label.config(text="Transcription complete!")
                self.master.show_screen("MarkdownViewerPage")
            else:
                self.status_label.config(text="Transcription failed.")

            os.unlink(temp_wav.name)  # Clean up

        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

    def transcribe_audio(self, file_path):
        """Send audio file to AssemblyAI and return transcription text."""
        headers = {'authorization': ASSEMBLYAI_API_KEY}

        # Step 1: Upload audio
        with open(file_path, 'rb') as f:
            upload_res = requests.post(
                'https://api.assemblyai.com/v2/upload',
                headers=headers,
                data=f
            )
        if upload_res.status_code != 200:
            return None
        upload_url = upload_res.json()['upload_url']

        # Step 2: Request transcription
        json_data = {'audio_url': upload_url}
        trans_res = requests.post(
            'https://api.assemblyai.com/v2/transcript',
            headers=headers,
            json=json_data
        )
        if trans_res.status_code != 200:
            return None
        transcript_id = trans_res.json()['id']

        # Step 3: Poll until done
        while True:
            poll_res = requests.get(
                f'https://api.assemblyai.com/v2/transcript/{transcript_id}',
                headers=headers
            )
            status = poll_res.json()['status']
            if status == 'completed':
                return f"# Lecture Transcription\n\n{poll_res.json()['text']}"
            elif status == 'error':
                return None
