# assets/images/images.py

import pygame
import os

def load_image(filename):
    filepath = os.path.join('assets', 'images', filename)
    return pygame.image.load(filepath)

def load_all_images():
    # List all image files you want to load
    image_files = ['image1.png', 'image2.png']  # Example, update accordingly
    images = {}
    for image_file in image_files:
        images[image_file] = load_image(image_file)
    return images
