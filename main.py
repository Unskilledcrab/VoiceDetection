from classes import ConversationBot, Audio2Sound, BackgroundAudioPlayer, Speech2Text
import time

def system_clip(name):
    return f"./audio_clips/system/{name}"

time.sleep(1)
background_audio = BackgroundAudioPlayer(system_clip("ambient_loop1-88046.mp3"))
background_audio.start()
speech_2_text = Speech2Text()
time.sleep(1)

conversation_bots = {    
    "lumpy": ConversationBot('Lumpy', 'you are a farmer and you love to talk about your farm and your family. You have a younger daughter delila', 'TxGEqnHWrfWFTfGW9XjX'),
    "elli": ConversationBot('Elli', 'You are a girl who is homeless and looking for your family. You are afraid and wanting to know how to find Arithra because that is where you last saw your mom.', 'MF3mGyEYCl7XYWbV9V6O')
}

Audio2Sound().play(system_clip("intro_orb.mp3"))

current_bot: ConversationBot = None

leave_intent = [
    "bye",
    "goodbye"
]

recall_intent = [
    "repeat what you said",
    "what did you say",
    "say that again"
]

help_intent = [
    "help"
    "what do I do"
]

def print_bot_names():
    for key in conversation_bots.keys():
        print(key)

def is_intent(message: str, intent_list) -> bool:
    for intent in intent_list:
        if intent in message.lower():
            return True
    return False

def handle_entry(message: str):
    global current_bot
    for key in conversation_bots.keys():
        if key in message.lower():
            print(f"now talking to {key}")
            current_bot = conversation_bots[key]
            Audio2Sound().play(system_clip("connecting_to_person.mp3"))
            return
    
    if is_intent(message, help_intent):
        print(f"Help Intent: {message}")
        Audio2Sound().play(system_clip("help.mp3"))
        return
    
    print("You must select a character to talk to from the following:")
    print_bot_names()
    Audio2Sound().play(system_clip("help.mp3"))
    
def handle_bot_intent(message: str):
    global current_bot
    if is_intent(message, leave_intent):
        print(f"Leave Intent: {message}")
        current_bot = None
        return
    if is_intent(message, recall_intent):
        print(f"Recall Intent: {message}")
        current_bot.replay()
        pass
    else:
        print("talking to bot")
        current_bot.talk_to(message)

def classify_speech(message: str):
    global current_bot
    if current_bot:        
        handle_bot_intent(message)
        return
    
    if not current_bot:
        handle_entry(message)

while True:
    print("listening...")
    captured_speech = speech_2_text.listen()
    #captured_speech = input("What did you say? ")   
    if captured_speech:
        classify_speech(captured_speech)
