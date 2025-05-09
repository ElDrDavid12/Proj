# Crear un rectángulo para el jugador
player_rect = pygame.Rect(x, y, 50, 50)

# Crear un rectángulo para el objetivo (como un enemigo o una meta)
target_rect = pygame.Rect(300, 300, 50, 50)

# Detectar colisión
if player_rect.colliderect(target_rect):
    print("¡Colisión detectada!")
