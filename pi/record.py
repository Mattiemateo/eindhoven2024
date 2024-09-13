import wave
import pyaudio
import time

# Function to record audio
def record_audio(output_filename, timeout=7):
    FORMAT = pyaudio.paInt16  # 16-bit resolution
    CHANNELS = 1              # Stereo channel (adjust if using mono)
    RATE = 44100              # 44.1kHz sampling rate
    CHUNK = 1024              # Increase chunk size to help with overflow issues

    # Initialize PyAudio object
    audio = pyaudio.PyAudio()

    start_time = time.time()
    current_time = time.time()

    try:
        # Start recording
        print("Recording...")
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []

        # Record for the specified duration
        while (current_time - start_time) < timeout * 1000:
            try:
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)
                current_time = time.time()

            except IOError as e:
                print(f"Error recording audio: {e}")
                break

        # Stop recording
        print("Finished recording.")
        stream.stop_stream()
        stream.close()

    except Exception as e:
        print(f"Error initializing stream: {e}")

    finally:
        audio.terminate()

    # Save the recorded audio as a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Saved recording as {output_filename}")