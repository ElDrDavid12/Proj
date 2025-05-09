import pygame
from core.scenes import SceneManager

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager(screen)
    
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.scene_manager.update()
            self.scene_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.scene_manager.handle_input(event)
        
        pygame.quit()
