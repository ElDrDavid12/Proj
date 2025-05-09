# main.py

import pygame
import sys
from config import WIDTH, HEIGHT, FPS, TITLE, CELL_SIZE
from snake import Snake
from food import Food

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
def game_loop():
    snake = Snake()  # Create a new snake object
    food = Food()    # Create a new food object

    # Main game loop
    while True:
        # Handle events (like quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle user input (direction changes)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake.direction != (CELL_SIZE, 0):
            snake.direction = (-CELL_SIZE, 0)
        if keys[pygame.K_RIGHT] and snake.direction != (-CELL_SIZE, 0):
            snake.direction = (CELL_SIZE, 0)
        if keys[pygame.K_UP] and snake.direction != (0, CELL_SIZE):
            snake.direction = (0, -CELL_SIZE)
        if keys[pygame.K_DOWN] and snake.direction != (0, -CELL_SIZE):
            snake.direction = (0, CELL_SIZE)

        # Move the snake
        snake.move()

        # Check if the snake eats food
        if snake.body[0] == food.position:
            snake.grow()  # Grow the snake
            food.spawn(snake.body)  # Spawn new food

        # Check for collisions (wall or self)
        if snake.check_collision():
            break  # Game over, exit the loop

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen (black background)
        snake.draw(screen)      # Draw the snake
        food.draw(screen)       # Draw the food

        # Update the display
        pygame.display.update()

        # Set the FPS
        clock.tick(FPS)

    # Game over, reset the game
    print("Game Over!")
    pygame.time.wait(1000)  # Wait a bit before restarting
    game_loop()  # Restart the game

# Start the game
if __name__ == "__main__":
    game_loop()
