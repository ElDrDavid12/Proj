import pygame
from core.npc import NPC
from core.utils import load_image
from core.clue import Clue

class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.current_scene = IntroScene(screen)

    def update(self):
        self.current_scene.update()

    def draw(self):
        self.current_scene.draw()

    def handle_input(self, event):
        self.current_scene.handle_input(event)

class IntroScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render("Welcome to the Black Dahlia Murder investigation.", True, (255, 255, 255))
        self.npc = NPC("Officer", "There's a clue nearby...")
        self.has_talked = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, (100, 100))
        if self.has_talked:
            self.npc.speak(self.screen)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.has_talked:
                self.has_talked = True
                self.text = self.font.render(self.npc.message, True, (255, 255, 255))
            elif event.key == pygame.K_RETURN and self.has_talked:
                # Transition to next scene (e.g., exploration or finding clues)
                print("Proceed with the investigation...")
