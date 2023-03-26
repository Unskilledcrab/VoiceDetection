from classes import ConversationBot, Audio2Sound

conversation_bot = ConversationBot('Larry', 'you are a farmer and you love to talk about your farm and your family. You have a younger daughter delila')
conversation_bot.SetListenSound('./audio_clips/system/ambient_loop1-88046.mp3')
conversation_bot.SetAcknowledgementSound('./audio_clips/system/acknowledge.mp3')
conversation_bot.SetSendingMessageSound('./audio_clips/system/dark-magic-loop-47178.mp3')

Audio2Sound().play("./audio_clips/system/intro_orb.mp3")

conversation_bot.Listen()