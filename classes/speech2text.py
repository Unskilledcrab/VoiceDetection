import speech_recognition as sr
import time

class Speech2Text:
    def __init__(self) -> None:
        # create a recognizer object
        self.r = sr.Recognizer()

    def listen(self, timeout = 30):
        start_time = time.time()
        # open the audio file
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            text = None
            while True:
                # Listen for audio
                audio = self.r.listen(source)

                # Use speech recognition to transcribe the audio
                try:
                    text = self.r.recognize_google(audio)
                    print(f"I heard: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

                elapsed_time = time.time() - start_time
                if elapsed_time >= timeout:
                    print(f"Timed out after {timeout} seconds")
                    return None
