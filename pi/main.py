import serial

from pi.record import record_audio
from pi.voice import exchange_audio

def main():
    global recording
    
    # Replace with your actual serial port
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    while True:
        # Send data to the ESP32 if needed
        # ser.write(b'Some Command\n')

        # Read the response from the ESP32
        response = ser.readline().decode('utf-8').strip()

        if response == "record":
            recording = True
            print("record!")
            output_filename = "input.wav"
            record_audio(output_filename)  # Record audio
            exchange_audio(output_filename, 'marv')  # Process the recorded audio

    ser.close()

# Run the main loop
if __name__ == "__main__":
    main()