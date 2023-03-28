## Getting started
navigate to the directory containing `requirements.txt`
```
pip install -r requirements.txt
```

On windows you may have to run
```
py -m pip install -r requirements.txt
```

make sure to add and set the following environmental variables

`CHATGPT_API_KEY` - You must setup an account at openai.com 
- go to https://platform.openai.com/account/api-keys to retrieve your key
- go to https://platform.openai.com/account/org-settings to get your org id and update chatbot.py with your org id

`ELEVEN_LABS_API_KEY` - You must setup an account at elevenlabs.io and do the following
- click on your profile in the top right corner
- select profile
- reveal and copy and paste your API key 

then run `main.py` or any of the tests to test individual components

#### Eleven Labs
Used for text to speech
https://beta.elevenlabs.io/speech-synthesis

#### OpenAI ChatGPT
Used for text generation (chat bot)
https://chat.openai.com/chat

#### SpeechRecognition
Used to capture audio and translate into text

#### playsound
Used for audio playback

#### Sound Effects
- Sound Effect from [Pixabay](https://pixabay.com/sound-effects/)