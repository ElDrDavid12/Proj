import pygame
import os

def play_sound(sound_name):
    """Plays a sound from the assets/sounds directory."""
    sound_path = os.path.join('assets', 'sounds', sound_name)
    if os.path.exists(sound_path):
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    else:
        print(f"Error: {sound_name} not found!")
