import pygame
import sys

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Variables de juego
paddle_width = 15
paddle_height = 100
ball_size = 15
speed = 5

# Posición de las palas
player_y = HEIGHT // 2 - paddle_height // 2
computer_y = HEIGHT // 2 - paddle_height // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = speed, speed

# Reloj
clock = pygame.time.Clock()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover la pala del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - paddle_height:
        player_y += speed

    # Mover la pala de la computadora
    if ball_y < computer_y + paddle_height // 2:
        computer_y -= speed
    if ball_y > computer_y + paddle_height // 2:
        computer_y += speed

    # Mover la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebote de la pelota en las paredes
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y

    # Rebote de la pelota en las palas
    if ball_x <= paddle_width and player_y < ball_y < player_y + paddle_height:
        ball_speed_x = -ball_speed_x
    if ball_x >= WIDTH - paddle_width - ball_size and computer_y < ball_y < computer_y + paddle_height:
        ball_speed_x = -ball_speed_x

    # Detectar si la pelota sale de la pantalla (anotación)
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x, ball_speed_y = speed, speed

    # Dibujar todo
    screen.fill((0, 0, 0))  # Fondo
    pygame.draw.rect(screen, (255, 255, 255), (0, player_y, paddle_width, paddle_height))  # Pala del jugador
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH - paddle_width, computer_y, paddle_width, paddle_height))  # Pala de la computadora
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_size)  # Pelota

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
