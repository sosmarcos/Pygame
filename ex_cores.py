import pygame
from pygame.locals import *

cor1 = (0, 140, 60)
cor2 = pygame.Color(255, 120, 9)

pygame.display.set_caption('Cores em pygame')
ventana = pygame.display.set_mode((400,300))
ventana.fill(cor2)

pygame.init()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    pygame.display.update()
