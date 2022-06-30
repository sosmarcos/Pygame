import pygame
from pygame.locals import *

pygame.display.set_caption('Carregando imagens em pygame')
ventana = pygame.display.set_mode((500,300))

  # load() serve para carregar arquivos
imagem = pygame.image.load('Eter_pin-up.png')
posX, posY = 0, 0

  # blit() serve para adicionar imagens no display
ventana.blit(imagem, (posX, posY))

pygame.init()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    pygame.display.update()
