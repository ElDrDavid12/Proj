import pygame
import json
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Load assets
from assets.images.images import load_all_images  # You can implement this based on your images

# Load story and save data
def load_json_data(file_path):
    """Utility function to load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_data(file_path, data):
    """Utility function to save JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Render text to the screen
def render_text(screen, text, position, font, color=(255, 255, 255)):
    """Render and display text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Main game loop
def game_loop():
    """Main game loop for displaying the story and interacting with the user."""
    # Initialize screen and font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Smiley Face Killers')
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    # Load the story and save data
    story = load_json_data('data/story.json')  # Load story directly from the root directory
    save_data = load_json_data('data/save_data.json')

    current_scene = save_data["current_scene"]

    # State tracking variables
    selected_option = 0

    while True:
        screen.fill((0, 0, 0))

        scene = story.get(current_scene)
        if scene is None:
            print(f"Error: Scene '{current_scene}' not found!")
            break

        # Display the scene description
        render_text(screen, scene['description'], (50, 50), font)

        # Display the options
        y_offset = 150
        for idx, option in enumerate(scene['options']):
            text = f"> {option['text']}" if idx == selected_option else f"  {option['text']}"
            render_text(screen, text, (50, y_offset + idx * 40), font)

        pygame.display.flip()

        # Event handling for user input
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(scene['options'])
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(scene['options'])
            elif event.key == pygame.K_RETURN:
                # Handle option selection
                next_scene = scene['options'][selected_option]['next_scene']
                current_scene = next_scene
                save_data["current_scene"] = current_scene
                save_json_data('data/save_data.json', save_data)

        clock.tick(FPS)

# Run the game
if __name__ == '__main__':
    game_loop()
