import pygame
from pygame.locals import *

pygame.display.set_caption('Utilizando a posição do cursor')
ventana = pygame.display.set_mode((700,300))

imagem = pygame.image.load('Opus_cruz.png')
posX = 0
posY = 0

velocidade = 5
direita = True

pygame.init()
while True:

    ventana.fill((255,255,255))
    ventana.blit(imagem, (posX, posY))
    
    posX = pygame.mouse.get_pos()[0] - 250
    posY = pygame.mouse.get_pos()[1] - 120
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
    pygame.display.update()
    