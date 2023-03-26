from classes import ChatBot

chatbot = ChatBot('Larry', 'you are a farmer named larry that loves to be welcoming and cherful')

while True:
    user_input = input("What would you like to say to larry? ")
    
    response = chatbot.SendMessage(user_input)