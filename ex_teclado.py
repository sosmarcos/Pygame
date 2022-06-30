import pygame
from pygame.locals import *

pygame.display.set_caption('Eventos de teclado em pygame')
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

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posX -= velocidade
            elif event.key == K_RIGHT:
                posX += velocidade
        
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                print('tecla esquerda')
            elif event.key == K_RIGHT:
                print('tecla direita')

    pygame.display.update()
    