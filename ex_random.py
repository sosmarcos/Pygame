import pygame
from pygame.locals import *
from random import randint

pygame.display.set_caption('Randomizando posições em pygame')
ventana = pygame.display.set_mode((500,300))

  # load() serve para carregar arquivos
imagem = pygame.image.load('Eter_pin-up.png')
posX = randint(10, 100)
posY = randint(10, 50)

  # blit() serve para adicionar imagens no display
ventana.blit(imagem, (posX, posY))

pygame.init()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    pygame.display.update()
