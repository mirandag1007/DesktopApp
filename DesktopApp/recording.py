import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sounddevice as sd
import wavio
import threading
import datetime
import os
import numpy as np
import requests
import time

# AssemblyAI API key from environment variable
ASSEMBLYAI_API_KEY = os.environ.get("ASSEMBLYAI_API_KEY")
HEADERS = {'authorization': ASSEMBLYAI_API_KEY}

class RecordingPage(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)

        tb.Label(self, text="Record Audio & Transcribe", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.fs = 44100
        self.recording = []
        self.is_recording = False
        self.filename = None
        self.start_time = None

        # --- Timer Label ---
        self.timer_label = tb.Label(self, text="00:00", font=("Helvetica", 18, "bold"))
        self.timer_label.pack(pady=5)

        # --- Buttons ---
        self.start_btn = tb.Button(self, text="Start Recording", bootstyle=SUCCESS, width=20, command=self.start_recording)
        self.start_btn.pack(pady=10)

        self.stop_btn = tb.Button(self, text="Stop Recording", bootstyle=DANGER, width=20, command=self.stop_recording, state="disabled")
        self.stop_btn.pack(pady=10)

        tb.Button(self, text="Back to Dashboard", bootstyle=INFO,
                  command=lambda: master.show_screen("DashboardPage")).pack(pady=10)

        # --- Text area for transcription/notes ---
        self.text_area = tb.Text(self, height=15, width=70)
        self.text_area.pack(pady=10)

    # --- Start recording ---
    def start_recording(self):
        self.is_recording = True
        self.recording = []
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="enabled")
        self.text_area.delete("1.0", "end")
        self.start_time = datetime.datetime.now()
        self._update_timer()
        threading.Thread(target=self._record_stream).start()

    # --- Timer update ---
    def _update_timer(self):
        if self.is_recording and self.start_time:
            elapsed = datetime.datetime.now() - self.start_time
            minutes, seconds = divmod(elapsed.seconds, 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self._update_timer)
        elif not self.is_recording:
            self.timer_label.config(text="00:00")

    # --- Recording stream ---
    def _record_stream(self):
        os.makedirs("recordings", exist_ok=True)

        def callback(indata, frames, time, status):
            if self.is_recording:
                self.recording.append(indata.copy())
            else:
                raise sd.CallbackStop()

        with sd.InputStream(samplerate=self.fs, channels=2, callback=callback):
            while self.is_recording:
                sd.sleep(100)

        # Combine chunks
        audio_data = np.concatenate(self.recording, axis=0)

        # Save WAV
        self.filename = f"recordings/recording_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        wavio.write(self.filename, audio_data, self.fs, sampwidth=2)

        # Re-enable buttons safely
        self.after(0, lambda: self.start_btn.config(state="enabled"))
        self.after(0, lambda: self.stop_btn.config(state="disabled"))
        self.after(0, lambda: self.timer_label.config(text="00:00"))

        # Transcribe
        threading.Thread(target=self._transcribe_audio).start()

    def stop_recording(self):
        self.is_recording = False

    # --- AssemblyAI transcription ---
    def _transcribe_audio(self):
        if not self.filename:
            self.after(0, lambda: self.text_area.insert("end", "❌ No audio file to transcribe.\n"))
            return

        self.after(0, lambda: self.text_area.insert("1.0", f"Saved recording to: {self.filename}\n"))
        self.after(0, lambda: self.text_area.insert("end", "Uploading and transcribing audio...\n"))

        try:
            # Upload audio
            with open(self.filename, 'rb') as f:
                upload_response = requests.post(
                    'https://api.assemblyai.com/v2/upload',
                    headers=HEADERS,
                    files={'file': f}
                )

            if upload_response.status_code != 200:
                self.after(0, lambda: self.text_area.insert("end", f"❌ Upload failed: {upload_response.status_code} {upload_response.text}\n"))
                return

            audio_url = upload_response.json().get('upload_url')
            if not audio_url:
                self.after(0, lambda: self.text_area.insert("end", f"❌ Upload response missing 'upload_url': {upload_response.text}\n"))
                return

            # Request transcription
            transcript_request = requests.post(
                'https://api.assemblyai.com/v2/transcript',
                headers=HEADERS,
                json={'audio_url': audio_url}
            )

            if transcript_request.status_code != 200:
                self.after(0, lambda: self.text_area.insert("end", f"❌ Transcription request failed: {transcript_request.status_code} {transcript_request.text}\n"))
                return

            transcript_id = transcript_request.json().get('id')
            if not transcript_id:
                self.after(0, lambda: self.text_area.insert("end", f"❌ No transcript ID returned: {transcript_request.text}\n"))
                return

            # Poll for completion
            while True:
                status_response = requests.get(f'https://api.assemblyai.com/v2/transcript/{transcript_id}', headers=HEADERS)
                try:
                    status_data = status_response.json()
                except Exception as e:
                    self.after(0, lambda: self.text_area.insert("end", f"❌ Failed to parse status response: {e}\n"))
                    return

                if status_data.get('status') == 'completed':
                    transcription = status_data.get('text', '')
                    self.after(0, lambda t=transcription: self.text_area.insert("end", "\n" + t))
                    break
                elif status_data.get('status') == 'failed':
                    self.after(0, lambda: self.text_area.insert("end", "❌ Transcription failed (AssemblyAI reported failure)\n"))
                    break

                # Show progress dot safely
                self.after(0, lambda: self.text_area.insert("end", "."))
                time.sleep(1)

        except Exception as e:
            self.after(0, lambda: self.text_area.insert("end", f"❌ Transcription failed: {e}\n"))
