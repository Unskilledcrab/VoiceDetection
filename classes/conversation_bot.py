from .chatbot import ChatBot
from .text2speech import Text2Speech
from .audio2sound import Audio2Sound
from .speech2text import Speech2Text
from .background_audio_player import BackgroundAudioPlayer

class ConversationBot:
        
    def __init__(self, name, backstory) -> None:
        self.text_2_speech = Text2Speech()
        self.audio_2_sound = Audio2Sound()
        self.speech_2_text = Speech2Text()
        self.chatbot = ChatBot(name=name, conversation_primer=self.__getPrimer(name, backstory))
    
    def __getPrimer(self, name, backstory):
        return (
            "you are incredibly direct and to the point. "
            f"your name is {name} you are concise and try to answer questions with just a sentence or two. "
            f"{backstory}"
        )
        
    def SetListenSound(self, audio_file):
        self.listen_sound = audio_file
    
    def SetAcknowledgementSound(self, audio_file):        
        self.acknowledgement_sound = audio_file
        
    def SetSendingMessageSound(self, audio_file):
        self.send_message_sound = audio_file
    
    def Listen(self):
        self.listen_audio = BackgroundAudioPlayer(self.listen_sound)
        self.listen_audio.start()
        while True:
            print(f"{self.chatbot.name} is listening...")
            captured_speech = self.speech_2_text.listen()   
            if captured_speech:
                self._TalkTo(captured_speech)
        
    def _TalkTo(self, message: str):
        # self.listen_audio.stop()
        
        acknowledgement_audio = BackgroundAudioPlayer(self.acknowledgement_sound)
        acknowledgement_audio.start()
        acknowledgement_audio.stop()
        
        send_message_audio = BackgroundAudioPlayer(self.send_message_sound)
        send_message_audio.start()
        
        response = self.chatbot.SendMessage(message)
        response_audio_file = self.text_2_speech.text_to_speech(response, self.chatbot.GetResponseAudioFile())
        send_message_audio.stop()
        
        send_message_audio.join()
        acknowledgement_audio.join()
        # self.listen_audio.join()
        self.audio_2_sound.play(response_audio_file)
        # self.audio_2_sound.play("./audio_clips/Joey/2.mp3")
        
        # self.listen_audio = BackgroundAudioPlayer(self.listen_sound)
        # self.listen_audio.start()
        