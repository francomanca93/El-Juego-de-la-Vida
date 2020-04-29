import sys, pygame

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

while True:

    # Creando rejilla
    for i in range(1, numberY_cells + 1):
        for j in range(1, numberX_cells + 1):
            poly = [
                ((j - 1) * dimensionCell_width, (i - 1) * dimensionCell_height),
                ((j) * dimensionCell_width,     (i - 1) * dimensionCell_height),
                ((j) * dimensionCell_width,     (i) * dimensionCell_height),
                ((j - 1) * dimensionCell_width, (i) * dimensionCell_height)
            ]

            pygame.draw.polygon(screen, color_cell,poly, width_line_cell)  # Dibujando rejilla

    pygame.display.flip()

