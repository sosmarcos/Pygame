import pygame
from pygame.locals import *

pygame.display.set_caption('Cores em pygame')
ventana = pygame.display.set_mode((700,300))


imagem = pygame.image.load('Opus_cruz.png')
posX = 0
posY = 0

velocidade = 1
direita = True

pygame.init()
while True:

    ventana.fill((255,255,255))
    ventana.blit(imagem, (posX, posY))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    if direita:
        if posX < 300:
            posX += velocidade
        else:
            direita = False
    else:
        if posX > 1:
            posX -= velocidade
        else:
            direita = True

    pygame.display.update()