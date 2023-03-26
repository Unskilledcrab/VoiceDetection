import playsound

class Audio2Sound:
    
    def __init__(self) -> None:
        pass    
    
    def play(self, audio_file_path: str, block: bool = True):
        print(f"playing audio: {audio_file_path}")
        playsound.playsound(audio_file_path, block)