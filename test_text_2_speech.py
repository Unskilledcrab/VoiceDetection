from classes import Text2Speech

text2speech = Text2Speech()

while True:
    user_input = input("What would you like to turn into speech? ")
    
    output_file = text2speech.text_to_speech(user_input)