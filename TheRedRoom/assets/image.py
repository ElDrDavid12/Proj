import pygame
import os

def load_image(image_name):
    """Loads an image from the assets/images directory."""
    image_path = os.path.join('assets', 'images', image_name)
    if os.path.exists(image_path):
        return pygame.image.load(image_path)
    else:
        print(f"Error: {image_name} not found!")
        return None

def display_image(image):
    """Displays the image in the game window."""
    if image:
        screen = pygame.display.set_mode((800, 600))  # Adjust size as needed
        screen.blit(image, (0, 0))  # Position at the top-left corner
        pygame.display.update()
