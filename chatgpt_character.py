import time
import keyboard
from rich import print
from azure_speech_to_text import SpeechToTextManager
from openai_chat import OpenAiManager
from eleven_labs import ElevenLabsManager
from audio_player import AudioManager

ELEVENLABS_VOICE = "Betty" # Replace this with the name of whatever voice you have created on Elevenlabs

BACKUP_FILE = "ChatHistoryBackup.txt"

elevenlabs_manager = ElevenLabsManager()
speechtotext_manager = SpeechToTextManager()
openai_manager = OpenAiManager()
audio_manager = AudioManager()

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
You are a fortune telling machine called Stanko The Soothsayer.
You are loosely based on the classic Zoltar fortune telling machines. 
Please use a variety of fortune telling sources of inspiration including but not limited to Madame Zita, the Magic 8 Ball, the Zoltar machine from the movie Big, Blavatsky, Estrella's Prophecies Fortune Teller, and the Oracle of Delphi.
                       
You will be asked a series of questions by the user regarding their own futures and must respond to be each question as the spirits, stars, and secret masters tell you too.
                        
While responding as Stanko The Soothsayer, you must obey the following rules: 
1) Provide short responses, about 1-2 paragraphs. 
2) Always stay in character, no matter what. 
3) Write and use new catchphrases that are fun observations about the current situations. 
4) Keep your answers limited to just a few sentences.
                        
Okay, let the conversation begin!'''}
openai_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

print("[green]Starting the loop, press F4 to begin")
while True:
    # Wait until user presses "f4" key
    if keyboard.read_key() != "f4":
        time.sleep(0.1)
        continue

    print("[green]User pressed F4 key! Now listening to your microphone:")

    # Get question from mic
    mic_result = speechtotext_manager.speechtotext_from_mic_continuous()
    
    # Send question to OpenAi
    openai_result = openai_manager.chat_with_history(mic_result)
    
    # Write the results to txt file as a backup
    with open(BACKUP_FILE, "w") as file:
        file.write(str(openai_manager.chat_history))

    # Send it to 11Labs to turn into cool audio
    elevenlabs_output = elevenlabs_manager.text_to_audio(openai_result, ELEVENLABS_VOICE, False)

    # Play the mp3 file
    audio_manager.play_audio(elevenlabs_output, True, True, True)

    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")
    
