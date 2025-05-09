import pygame

def load_image(path):
    """Helper function to load an image."""
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error:
        print(f"Error loading image: {path}")
        return None
