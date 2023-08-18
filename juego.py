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
aqua = (0, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
muddy_color = (80, 80, 80)  # Color del fondo cuando el juego se vuelve difícil

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

# Bolas de agua
waterball_radius = 15
waterball_speed = 2
waterballs = []
waterball_points = 0

# Bolas amarillas (poder)
powerball_radius = 10
powerballs = []
powerball_timer = 0
powerball_cooldown = 10 * 60  # 10 segundos en frames

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Temporizador
game_time = 0
font = pygame.font.Font(None, 36)
timer_text = font.render("Time: 0", True, red)
timer_rect = timer_text.get_rect(center=(window_width // 2, 20))

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

    # Generar bolas de agua aleatorias
    if random.randint(0, 100) < 2:
        waterballs.append([random.randint(0, window_width - waterball_radius * 2), -waterball_radius * 2])

    # Generar bolas amarillas (poder)
    if powerball_timer <= 0 and random.randint(0, 100) < 3:
        powerballs.append([random.randint(0, window_width - powerball_radius * 2), -powerball_radius * 2])
        powerball_timer = 10 * 60  # 10 segundos en frames

    # Mover bolas de fuego
    for fireball in fireballs:
        fireball[1] += fireball_speed

    # Mover bolas de agua
    for waterball in waterballs:
        waterball[1] += waterball_speed

    # Mover bolas amarillas (poder)
    for powerball in powerballs:
        powerball[1] += fireball_speed

    # Verificar colisiones con bolas de fuego
    for fireball in fireballs:
        if character_x < fireball[0] + fireball_radius and character_x + character_width > fireball[0] and \
           character_y < fireball[1] + fireball_radius and character_y + character_height > fireball[1]:
            pygame.quit()
            sys.exit()

    # Verificar colisiones con bolas de agua
    for waterball in waterballs:
        if character_x < waterball[0] + waterball_radius and character_x + character_width > waterball[0] and \
           character_y < waterball[1] + waterball_radius and character_y + character_height > waterball[1]:
            waterballs.remove(waterball)
            waterball_points += 1

    # Verificar colisiones con bolas amarillas (poder)
    for powerball in powerballs:
        if character_x < powerball[0] + powerball_radius and character_x + character_width > powerball[0] and \
           character_y < powerball[1] + powerball_radius and character_y + character_height > powerball[1]:
            powerballs.remove(powerball)
            powerball_timer = powerball_cooldown
            character_speed += 1

    # Actualizar temporizador
    game_time += 1
    timer_text = font.render(f"Time: {game_time // 60}", True, red)

    window.fill(black)

    # Cambiar el fondo si el juego se vuelve difícil
    if game_time > 300:
        window.fill(muddy_color)

    # Dibujar personaje
    pygame.draw.rect(window, red, (character_x, character_y, character_width, character_height))

    # Dibujar bolas de fuego
    for fireball in fireballs:
        pygame.draw.circle(window, red, (fireball[0] + fireball_radius, fireball[1] + fireball_radius), fireball_radius)

    # Dibujar bolas de agua
    for waterball in waterballs:
        pygame.draw.circle(window, aqua, (waterball[0] + waterball_radius, waterball[1] + waterball_radius), waterball_radius)

    # Dibujar bolas amarillas (poder)
    for powerball in powerballs:
        pygame.draw.circle(window, yellow, (powerball[0] + powerball_radius, powerball[1] + powerball_radius), powerball_radius)

    # Dibujar temporizador
    window.blit(timer_text, timer_rect)

    pygame.display.update()
    clock.tick(60)  # 60 FPS

pygame.quit()