# food.py

import pygame
import random
from config import CELL_SIZE, WIDTH, HEIGHT, RED

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn([])  # Call spawn to set an initial position

    def spawn(self, snake_body):
        # Ensure food does not spawn on the snake's body
        while True:
            self.position = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )
            if self.position not in snake_body:
                break  # Exit loop when valid food position is found

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)  # Food color
