import sys, pygame
import numpy as np
import matplotlib.pyplot as plt
import time

pygame.init()  # Inicializa todos los modulos pygame importados

# ---------- Settings ----------
size = width, height = 600, 600  # Tamaño de pantalla

# Definiendo cantidad de celdas que tendra la pantalla
numberX_cells = 60  # Numero de celdas en x
numberY_cells = 60  # Numero de celdas en y

# Dimension de celdas
dimensionCell_width = (width - 1) / numberX_cells
dimensionCell_height = (height- 1) / numberY_cells

background = 25, 25, 25  # Color de fondo
color_cell = (128, 128, 128) # Color de la rejilla de las celdas
width_line_cell = 1  # Ancho de la linea para las celdas
screen = pygame.display.set_mode(size)  # Pantalla

screen.fill(background)  #  

# Inicializamos todas las celdas en 0
gameState = np.zeros((numberX_cells, numberY_cells))

# Estado inicial. Creacion del automata celuar simple. Ponemos a 1 los siguientes estados 
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

while True:

    # Para cerrar la ventana desde la x superior
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This event gets me access to close the window
            sys.exit()

    # Actualizo estado. Nuevo estado sera una copia de gameState
    new_gameState = np.copy(gameState)

    # Actualizo la pantalla. Para ver el movimiento del automata celular
    screen.fill(background)

    # Creando rejilla
    for y in range(0, numberY_cells):
        for x in range(0, numberY_cells):
            
            # Calculo el numero de vecinos alrededor de la celda dada por el ciclo
            n_neigh = gameState[(x - 1) % numberX_cells, (y - 1) % numberY_cells] + \
                      gameState[(x    ) % numberX_cells, (y - 1) % numberY_cells] + \
                      gameState[(x + 1) % numberX_cells, (y - 1) % numberY_cells] + \
                      gameState[(x - 1) % numberX_cells, (y    ) % numberY_cells] + \
                      gameState[(x + 1) % numberX_cells, (y    ) % numberY_cells] + \
                      gameState[(x - 1) % numberX_cells, (y + 1) % numberY_cells] + \
                      gameState[(x    ) % numberX_cells, (y + 1) % numberY_cells] + \
                      gameState[(x + 1) % numberX_cells, (y + 1) % numberY_cells]

            # ----- REGLAS DEL JUEGO DE LA VIDA -----

            # Una célula muerta con exactamente 3 células vecinas vivas "nace".
            if gameState[x, y] == 0 and n_neigh == 3:
                new_gameState[x, y] = 1
            # Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                new_gameState[x, y] = 0
            
            # Dibujamos las condiciones anteriores
            poly = [
                ((x) * dimensionCell_width, (y) * dimensionCell_height),
                ((x + 1) * dimensionCell_width,     (y) * dimensionCell_height),
                ((x + 1) * dimensionCell_width,     (y + 1) * dimensionCell_height),
                ((x) * dimensionCell_width, (y + 1) * dimensionCell_height)
            ]

            # Dibujando rejilla con el automata actualizado
            pygame.draw.polygon(screen, color_cell, poly, int(abs(1 - new_gameState[x, y])))

    # Actualizamos el estado del juego. 
    gameState = new_gameState
    time.sleep(0.1)
    pygame.display.flip()

