import pygame

class NPC:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.font = pygame.font.Font(None, 24)

    def speak(self, screen):
        text = self.font.render(f"{self.name}: {self.message}", True, (255, 255, 255))
        screen.blit(text, (100, 200))
