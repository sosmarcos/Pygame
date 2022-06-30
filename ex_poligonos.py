import pygame
from pygame.locals import *

pygame.display.set_caption('Cores em pygame')
ventana = pygame.display.set_mode((400,300))

pygame.draw.circle(ventana, (8, 70, 120), (80, 90), 20)
  # ===Circulo=== (display, (  cor RGB ), (centro), raio)

pygame.draw.rect(ventana, (130, 70, 70), (0, 0, 100, 50))
  # =Retangulo= (display, (  cor RGB ),  (X, Y, larg,  Alt))

pygame.draw.polygon(ventana, (90, 100, 70), ((80,90),(150,100),(60,80)))
  # ===Poligono=== (display, (  cor RGB  ), ((x1,y1),(x2,y2),(x3,y3)))

pygame.draw.polygon(ventana, (90, 100, 70), ((140,0),(291,106),(237,277),(56,277),(0,106)))

pygame.init()
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

    pygame.display.update()
