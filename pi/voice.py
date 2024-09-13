import requests
from pydub.playback import play

from audio import convert_mp3_to_wav, play_audio

API_URL = "http://192.168.3.234:5000"

# Function to switch personality
def switch_personality(new_personality):
    api_url = f"{API_URL}/switch_personality"
    response = requests.post(api_url, json={"personality": new_personality})

    if response.status_code == 200:
        print(f"Switched to {new_personality.capitalize()}")
    else:
        print("Error switching personality:", response.status_code, response.text)

# Function to process audio
def exchange_audio(audio_file_path, new_personality):
    api_url = f"{API_URL}/process_audio"

    mp3 = False
    playfile = ""

    with open(audio_file_path, 'rb') as audio_file:
        files = {'audio': audio_file}
        response = requests.post(api_url, files=files)

    if response.status_code == 200:
        if new_personality == 'glados':
            response_file_path = "response_g.wav"
            playfile  = "response_g.wav"
        elif new_personality == 'marv':
            mp3 = True
            response_file_path = "response.mp3"
            playfile  = "response_m.wav"

        with open(response_file_path, "wb") as f:
            f.write(response.content)
        print("Received and saved response.wav.")
        if mp3:
            convert_mp3_to_wav(response_file_path, playfile)

        play_audio(playfile)  # Play the saved audio file
    else:
        print("Error processing audio:", response.status_code, response.text)