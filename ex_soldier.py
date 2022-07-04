import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Animação em pygame')
window = pygame.display.set_mode((1000, 400))
soldier = pygame.image.load(f'sprits/Soldier_parado_esquerda_1.png')

arial = pygame.font.SysFont('Arial', 10)

fluides = 30
posX = 970
posY = 200
desloc = 2
frame = 0

parado_esquerda = True
parado_direita = False
esquerda = False
direita = False
pulo_esquerda = False
pulo_direita = False

contador = 1
while True:
    tempo = int(pygame.time.get_ticks())
    relogio = arial.render(f'Tempo: {tempo/100}', 0, (255, 255, 255))
    quadro = arial.render(f'Frame: {frame}', 0, (255, 255, 255))
    
    if parado_esquerda and tempo % (fluides+60) == 0:
        frame += 1
        if frame == 8:
            frame = 1

        soldier = pygame.image.load(f'sprits/Soldier_parado_esquerda_{frame}.png')

    if parado_direita and tempo % (fluides+60) == 0:
        frame += 1
        if frame == 8:
            frame = 1

        soldier = pygame.image.load(f'sprits/Soldier_parado_direita_{frame}.png')

    if direita and tempo % fluides == 0:  # se o deslocamento a direita estiver ativo
        frame += 1
        if frame == 13:
            frame = 1

        soldier = pygame.image.load(f'sprits/Soldier_direita_{frame}.png')
        posX += desloc

    if esquerda and tempo % fluides == 0:  # se o deslocamento a esquerda estiver ativo
        frame += 1
        if frame == 13:
            frame = 1
        
        soldier = pygame.image.load(f'sprits/Soldier_esquerda_{frame}.png')
        posX -= desloc

    window.fill((0, 0, 0))
    pygame.draw.line(window, (20, 20, 20), (0, 243), (1000, 243), 4)
    window.blit(soldier, (posX, posY))
    window.blit(relogio, (10, 20))
    window.blit(quadro, (11, 35))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:  # se uma tecla for precionada
            if event.key == K_a and not direita:  # se a tecla for A e não D
                esquerda = True
                parado_esquerda = False
                parado_direita = False

            elif event.key == K_d and not esquerda:  # se a tecla for D e não A
                direita = True
                parado_esquerda = False
                parado_direita = False

        elif event.type == pygame.KEYUP:  # se uma tecla for solta
            if event.key == K_a and not direita:
                esquerda = False
                parado_esquerda = True
                frame = 0

            elif event.key == K_d and not esquerda:
                direita = False
                parado_direita = True
                frame = 0

    pygame.display.update()
