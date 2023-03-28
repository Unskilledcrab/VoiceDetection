from datetime import datetime
import requests
import os

class Text2Speech:
    voice_id_lookup = {
        "premade/Adam": "pNInz6obpgDQGcFmaJgB",
        "premade/Antoni": "ErXwobaYiN019PkySvjV",
        "premade/Arnold": "VR6AewLTigWG4xSOukaG",
        "premade/Josh": "TxGEqnHWrfWFTfGW9XjX",
        "premade/Elli": "MF3mGyEYCl7XYWbV9V6O"       
    }
    
    def __init__(self) -> None:
        self.url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        self.voice_id = self.voice_id_lookup["premade/Adam"]
        self.api_key = os.environ['ELEVEN_LABS_API_KEY']
        self.headers = {            
            "Content-Type": "application/json",
            "xi-api-key" : self.api_key
        }
        
    def text_to_speech(self, text: str, output_file_path: str = None, voice_id: str = None):
        if not voice_id:
            voice_id = self.voice_id
            
        if not output_file_path:
            time_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            output_file_path = f"./audio_clips/{time_string}_{voice_id}.mp3"
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            
        print(f"sending message to convert to speech: {text}")
        data = {"text": text}
        response = requests.post(self.url.format(voice_id=voice_id), headers = self.headers, json = data)
        
        if response.status_code == 200:
            print(f"saving audio file: {output_file_path}")
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            with open(output_file_path, 'wb') as f:
                f.write(response.content)
            return output_file_path
        else:
            print("ERROR: Eleven Labs api call failed: ", response.status_code)