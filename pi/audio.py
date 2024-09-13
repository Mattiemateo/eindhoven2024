import os
from pydub import AudioSegment
from pydub.playback import play

# Function to play audio
def play_audio(file_path):
    if os.path.exists(file_path):
        print(f"Playing {file_path}...")
        audio = AudioSegment.from_wav(file_path)
        play(audio)
    else:
        print(f"File {file_path} does not exist!")

# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")
    print(f"Converted {mp3_file_path} to {wav_file_path}")

# Function to list audio input devices
def list_audio_devices():
    import pyaudio
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']} - Input Channels: {info['maxInputChannels']}")