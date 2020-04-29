import sys, pygame

pygame.init()  # Inicializa todos los modulos pygame importados

size = width, height = 600, 600  # Tamaño de pantalla

background = 25, 25, 25  # Colo de fondo

screen = pygame.display.set_mode(size)  # Pantalla

while True:

    screen.fill(background)
    pygame.display.flip()

