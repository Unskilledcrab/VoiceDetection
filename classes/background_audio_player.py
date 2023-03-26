import threading
from playsound import playsound

class BackgroundAudioPlayer(threading.Thread):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            playsound(self.filepath, block=True)

    def stop(self):
        self.stop_event.set()