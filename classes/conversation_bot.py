from .chatbot import ChatBot
from .text2speech import Text2Speech
from .audio2sound import Audio2Sound
from .speech2text import Speech2Text
from .background_audio_player import BackgroundAudioPlayer

class ConversationBot:
        
    def __init__(self, name, backstory, voice_id) -> None:
        self.text_2_speech = Text2Speech()
        self.audio_2_sound = Audio2Sound()
        self.speech_2_text = Speech2Text()
        self.voice_id = voice_id
        self.chatbot = ChatBot(name=name, conversation_primer=self.__get_primer(name, backstory))
        self.acknowledgement_sound = './audio_clips/system/acknowledge.mp3'
        self.send_message_sound = './audio_clips/system/dark-magic-loop-47178.mp3'
    
    def __get_primer(self, name, backstory):
        return (
            "You are incredibly concise and direct and try to answer questions with just a sentence or two. "
            f"Your name is {name} and when asked what your name is, you will respond 'my name is {name}' "
            "When you are asked questions, you will first consider your backstory. "
            f"This is your backstory: {backstory}"
        )
    
    def set_acknowledgement_sound(self, audio_file):        
        self.acknowledgement_sound = audio_file
        
    def set_sending_message_sound(self, audio_file):
        self.send_message_sound = audio_file
        
    # replay the last message
    def replay(self):
        response_audio_file = self.chatbot.get_response_audio_file()
        self.audio_2_sound.play(response_audio_file)
        
    def talk_to(self, message: str):        
        acknowledgement_audio = BackgroundAudioPlayer(self.acknowledgement_sound)
        acknowledgement_audio.start()
        acknowledgement_audio.stop()
        
        send_message_audio = BackgroundAudioPlayer(self.send_message_sound)
        send_message_audio.start()
        
        response = self.chatbot.send_message(message)
        response_audio_file = self.text_2_speech.text_to_speech(response, self.chatbot.get_response_audio_file(), self.voice_id)
        send_message_audio.stop()
        
        send_message_audio.join()
        acknowledgement_audio.join()
        self.audio_2_sound.play(response_audio_file)
        