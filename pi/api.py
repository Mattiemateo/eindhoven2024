from .record import record_audio
from .voice import exchange_audio, switch_personality

# Main loop
def main():
    personality = 'glados'
    switch_personality(personality)  # Switch to GLaDOS

    while True:
        command = input("Enter 'q' to record your question, or 'v' to switch voice, or 'exit' to quit: ").strip().lower()

        if command == 'q':
            output_filename = "input.wav"
            record_audio(output_filename)  # Record audio
            exchange_audio(output_filename, personality)  # Process the recorded audio

        elif command == 'exit':
            print("Exiting...")
            break

        elif command == 'v':
            voice = input("Press '1' to select Glados, or '2' for selecting Marv  ")
            if voice == '1':
                personality = 'glados'
            elif voice == '2':
                personality = 'marv'
            else:
                print("Invalid command. Please enter '1' to select Glados, or '2' for selecting Marv  ")
            switch_personality(personality)


        else:
            print("Invalid command. Please enter 'q' to record, or 'v' to switch voice, or 'exit' to quit.  ")

# Run the main loop
if __name__ == "__main__":
    main()
