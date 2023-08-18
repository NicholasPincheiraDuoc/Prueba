import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dodge the Fireballs")

# Colores
red = (255, 0, 0)
black = (0, 0, 0)

# Personaje
character_width = 50
character_height = 50
character_x = window_width // 2 - character_width // 2
character_y = window_height - character_height - 10
character_speed = 5

# Bolas de fuego
fireball_radius = 20
fireball_speed = 2
fireballs = []

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Loop del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # Generar bolas de fuego aleatorias
    if random.randint(0, 100) < 5:
        fireballs.append([random.randint(0, window_width - fireball_radius * 2), -fireball_radius * 2])

    # Mover bolas de fuego
    for fireball in fireballs:
        fireball[1] += fireball_speed

    # Verificar colisiones
    for fireball in fireballs:
        if character_x < fireball[0] + fireball_radius and character_x + character_width > fireball[0] and \
           character_y < fireball[1] + fireball_radius and character_y + character_height > fireball[1]:
            pygame.quit()
            sys.exit()

    window.fill(black)

    # Dibujar personaje
    pygame.draw.rect(window, red, (character_x, character_y, character_width, character_height))

    # Dibujar bolas de fuego
    for fireball in fireballs:
        pygame.draw.circle(window, red, (fireball[0] + fireball_radius, fireball[1] + fireball_radius), fireball_radius)

    pygame.display.update()
    clock.tick(60)  # 60 FPS

pygame.quit()