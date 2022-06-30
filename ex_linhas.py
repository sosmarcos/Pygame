import pygame
from pygame.locals import *

pygame.display.set_caption('Linhas em pygame')
ventana = pygame.display.set_mode((400,300))

cor = pygame.Color(60, 80, 150)
pygame.draw.line(ventana, cor, (60, 80), (160, 100), 8)

pygame.init()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    pygame.display.update()
