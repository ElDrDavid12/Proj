# Coordenadas del jugador
x, y = 100, 100
speed = 5

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectar teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Rellenar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el jugador (rectángulo)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(60)
