from classes import Speech2Text

speech2text = Speech2Text()

while True:    
    text = speech2text.listen()
    
    print(f"I heard you say: {text}")
    