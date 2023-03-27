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
    "larry": ConversationBot('Larry', 'you are a farmer and you love to talk about your farm and your family. You have a younger daughter delila')
}

Audio2Sound().play(system_clip("intro_orb.mp3"))

current_bot: ConversationBot = None

leave_intent = [
    "bye"
]

recall_intent = [
    "remind me"
]

help_intent = [
    "help"
]

def is_intent(message: str, intent_list) -> bool:
    for intent in intent_list:
        if intent in message:
            return True
    return False

def handle_entry(message: str):
    global current_bot
    for key in conversation_bots:
        if key in message:
            print(f"now talking to {key}")
            current_bot = conversation_bots[key]
            return
        
    print("You must select a character to talk to")
    Audio2Sound().play(system_clip("select_character.mp3"))
    
def handle_bot_intent(message: str):
    global current_bot
    if is_intent(message, leave_intent):
        print(f"Leave Intent: {message}")
        current_bot = None
        return
    if is_intent(message, help_intent):
        print(f"Help Intent: {message}")
        Audio2Sound().play(system_clip("help.mp3"))
        return
    if is_intent(message, recall_intent):
        print(f"Recall Intent: {message}")
        # make a method on bot to recall and replay past messages
        pass
    else:
        print("talking to bot")
        #current_bot.talk_to(message)

def classify_speech(message: str):
    global current_bot
    if current_bot:        
        handle_bot_intent(message)
    
    if not current_bot:
        handle_entry(message)

while True:
    print("listening...")
    #captured_speech = speech_2_text.listen()
    captured_speech = input("What did you say? ")   
    if captured_speech:
        classify_speech(captured_speech)
