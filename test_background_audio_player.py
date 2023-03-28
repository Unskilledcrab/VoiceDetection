from classes import BackgroundAudioPlayer

background_audio_player = BackgroundAudioPlayer("./audio_clips/system/voice.mp3")

background_audio_player.start()

while True:
    user_input = input("What would you like it to stop??? ")
    if "yes" in user_input:
        background_audio_player.stop()
        background_audio_player.join()
        break
    else:
        print(f"you didn't say yes: {user_input}")