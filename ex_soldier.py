import pygame
from pygame.locals import *

pygame.display.set_caption('Animação em pygame')
window = pygame.display.set_mode((400, 400))

soldier = pygame.image.load('spriters/Soldier_1.png')
posX = 200
desloc = 1
frame = 1
frame_direc = True

pygame.init()
while True:

    window.fill((0, 0, 0))
    window.blit(soldier, (posX, 200))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN and event.key == K_a:
            if frame_direc:
                frame += 1
                if frame == 11:
                    frame = 2
                    
            soldier = pygame.image.load(f'spriters/Soldier_{frame}.png')
            posX -= desloc
    pygame.display.update()
