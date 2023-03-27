import openai
import os
import json

class ChatBot:
    def __init__(self, name = "chatbot", conversation_primer = None, conversation_folder = "./conversations") -> None:
        self.openai = openai
        self.openai.organization = "org-v7bAIQ173wcb1j424hIAFUwH"
        self.openai.api_key = os.getenv('CHATGPT_API_KEY')
        self.name = name
        self.conversation = []
        self.active_file = f"{conversation_folder}/active/{name}.conv"
        self.archive_file = f"{conversation_folder}/archive/{name}.conv"
        self.audio_folder = f"./audio_clips/{name}"
        if conversation_primer:
            self.conversation.append(self._gpt_message('system', conversation_primer))
        self.__load_conversation()
        print(f"Created Chatbot: {name}")

    def _gpt_message(self, role, content):
        return {"role": role, "content": content}
                
    def get_audio_folder(self):
        return self.audio_folder
    
    def __load_conversation(self):
        if not os.path.exists(self.active_file):
            return
        
        with open(self.active_file, "r") as f:
            self.conversation = json.load(f)
            print(f"loaded previous conversation: {self.conversation}")
            
    def __save_conversation(self):
        os.makedirs(os.path.dirname(self.active_file), exist_ok=True)
        with open(self.active_file, "w") as f:
            json.dump(self.conversation, f)
        
    def reset_conversation(self):
        os.makedirs(os.path.dirname(self.archive_file), exist_ok=True)
        os.replace(self.active_file, self.archive_file)
        
    def get_conversation_index(self):
        return len(self.conversation)
    
    def get_response_audio_file(self):
        return f"{self.get_audio_folder()}/{self.get_conversation_index()}.mp3"
    
    def send_message(self, content) -> str:
        print(f"sending message to bot {self.name}: {content}")
        self.conversation.append(self._gpt_message('user',content))
        completion = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation,
            max_tokens=70
        )
        response = completion.choices[0].message.content
        print(f"bot {self.name} responded: {response}")
        self.conversation.append(self._gpt_message('assistant', response))
        self.__save_conversation()
        return response
