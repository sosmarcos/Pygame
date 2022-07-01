import pygame
from pygame.locals import *

pygame.display.set_caption('Colisões em pygame')
ventana = pygame.display.set_mode((700, 300))

velocidade = 1
direita = True
posX = 0
posY = 0

retângulo_1 = pygame.Rect(0, 0, 100, 50)
retângulo_2 = pygame.Rect(0, 120, 100, 50)

pygame.init()
while True:
    ventana.fill((0 ,0 ,0 ))
    
    pygame.draw.rect(ventana, (180, 70, 70), retângulo_1)
    pygame.draw.rect(ventana, (70, 180, 70), retângulo_2)

    retângulo_1.left, retângulo_1.top = pygame.mouse.get_pos()
    # left é a coordenada X do retângulo, e top a coordenada Y

    if retângulo_1.colliderect(retângulo_2):
        velocidade = 0

    else:
        velocidade = 1

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    if direita:
        if posX < 600:
            posX += velocidade
            retângulo_2.left = posX
        else:
            direita = False
    else:
        if posX > 1:
            posX -= velocidade
            retângulo_2.left = posX
        else:
            direita = True

    pygame.display.update()
    