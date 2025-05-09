# snake.py

import pygame
from config import WIDTH, HEIGHT, CELL_SIZE, GREEN, BLUE

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial positions
        self.direction = (CELL_SIZE, 0)  # Initial direction (right)
        self.length = 3  # Initial length of the snake

    def move(self):
        # Create a new head based on the current direction
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)  # Add the new head to the snake

        # If snake has eaten, don't remove the last segment
        if len(self.body) > self.length:
            self.body.pop()  # Remove the last segment

    def grow(self):
        self.length += 1  # Increase the length when eating food

    def check_collision(self):
        # Check if the snake hits the boundaries of the screen
        if self.body[0][0] < 0 or self.body[0][0] >= WIDTH or self.body[0][1] < 0 or self.body[0][1] >= HEIGHT:
            return True
        
        # Check if the snake collides with itself
        if self.body[0] in self.body[1:]:
            return True
        
        return False

    def draw(self, surface):
        # Draw each segment of the snake
        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)  # Snake color
            pygame.draw.rect(surface, BLUE, rect, 2)  # Border color (optional)
