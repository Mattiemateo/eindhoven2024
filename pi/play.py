import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load your audio file
pygame.mixer.music.load('client/input.wav')

# Play the audio file
pygame.mixer.music.play()

# Keep the script running while the audio plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
