import pygame
import time

# Initialize the pygame mixer for sounds
pygame.mixer.init()

# Load sound effects
footstep_sound = pygame.mixer.Sound('footsteps.wav')  # Path to your sound file
scream_sound = pygame.mixer.Sound('scream.wav')

# Play background music (looped)
pygame.mixer.music.load('background_music.mp3')  # Path to music file
pygame.mixer.music.play(loops=-1, fade_ms=1000)  # Loops indefinitely

# Play a footstep sound during the game (e.g., when a player moves)
footstep_sound.play()

# Wait for 2 seconds, then play a scream sound for added shock effect
time.sleep(2)
scream_sound.play()

# Wait for user input to end the game
input("Press Enter to exit the game...")

# Stop the music
pygame.mixer.music.stop()
pygame.quit()
