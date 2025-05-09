import pygame
from core.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Black Dahlia Murder")
    
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
