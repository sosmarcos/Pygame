import pygame
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('Textos em pygame')

moby_dick = pygame.font.Font('moby_dick/Moby DIck.ttf', 60)
texto1 = moby_dick.render('Ola Mundo', 0, (200, 60, 80))

arial = pygame.font.SysFont('Arial', 30)

circulo_X, circulo_Y = 15, 250


direita = True
velocidade = 1

while True:
    ventana.fill((0, 0, 0))

    circulo = pygame.draw.circle(ventana, (13, 70, 200), (circulo_X, circulo_Y), 15)
    cursor = pygame.draw.circle(ventana, (14, 170, 250), pygame.mouse.get_pos(), 15)
    texto2 = arial.render(f'Eixo X: {circulo_X}', 0, (200, 60, 80))

    ventana.blit(texto1, (80, 10))
    ventana.blit(texto2, (80, 70))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    if cursor.colliderect(circulo):
        velocidade = 0
    else:
        velocidade = 1

    if direita:
        if circulo_X < 385:
            circulo_X += velocidade
        else:
            direita = False

    else:
        if circulo_X > 15:
            circulo_X -= velocidade
        else:
            direita = True

    pygame.display.update()
