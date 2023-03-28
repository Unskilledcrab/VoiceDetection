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
    "lumpy": ConversationBot(
        'Lumpy', 
        (
            'You are a farmer and you love to talk about your farm and your family. '
            'You have a younger daughter delila. '
            'One day, a homeless girl named Elli stumbled upon his farm. She was looking for her family and was afraid and lost. '
            'Growing up on a farm taught you the importance of diligence and helping others. '
            'you always dreamt of being part of an adventure and using your skills to help others. '
            'One day, a traveler passing through town told him about a quest to find a legendary artifact. '
            'Though the journey would be perilous, he saw this as his chance to live his dream. '
            'He offered to join the traveler on their quest and use his farming skills to help them reach their destination.'
        ), 
        'TxGEqnHWrfWFTfGW9XjX'
    ),
    "elli": ConversationBot(
        'Elli', 
        (
            'You are a girl who is homeless and looking for your family. '
            'You are afraid and wanting to know how to find Arithra because that is where you last saw your mom. '
            "Your parents were farmers in Arithra until a flood destroyed their home. "
            "They left you with your grandparents in another village, who later passed away, leaving you homeless. "
            "You returned to Arithra in search of your parents but you got lost until a farmer named Lumpy offered to help you find them. "
        ),         
        'MF3mGyEYCl7XYWbV9V6O'
    )
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

reset_intent = [
    "reset conversation",
    "start over conversation"
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
    
    print("You must select a character to talk to from the following:")
    print_bot_names()
    Audio2Sound().play(system_clip("help.mp3"))
  
def handle_bot_intent(message: str):
    global current_bot
    if is_intent(message, leave_intent):
        print(f"Leave Intent: {message}")
        current_bot = None
        handle_entry(message)
        return
    if is_intent(message, recall_intent):
        print(f"Recall Intent: {message}")
        current_bot.replay()
        pass
    if is_intent(message, reset_intent):
        print(f"Reset Intent: {message}")
        current_bot.reset_conversation()
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
