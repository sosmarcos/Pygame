import pygame
from pygame.locals import *

pygame.init()


class Animação:
    def __init__(self, imagem, quadros, desloc, fluides):
        self.imagem = imagem
        self.quadros = quadros
        self.X = desloc[0]
        self.Y = desloc[1]
        self.frame = 1
        self.fluides = fluides
        self.ativo = False


    def on(self, tempo, sujeito=None):
        if tempo%self.fluides == 0:
            self.frame += 1
            if self.frame == self.quadros and self.Y:
                self.ativo = False
                
                if self.X == 0:
                    sujeito.repouso = True
                else:
                    self.X = 0

            elif self.frame > self.quadros:
                self.frame = 1
                
            global posX, posY
            posX += self.X
            if self.frame <= self.quadros//2:
                posY += self.Y
                print(self.Y)
                
            elif self.quadros > self.frame > self.quadros//2:
                posY += (self.Y - (self.Y + self.Y))
                print(self.Y - (self.Y + self.Y))
            
        global window
        quadro = arial.render(f'Frame: {self.frame}', 0, (255, 255, 255))
        window.blit(quadro, (10, 72))

        return pygame.image.load(f'{self.imagem}{self.frame}.png')


class Personagem:
    def __init__(self, nome, alinhamento='esquerda'):
        self.nome = nome
        self.alinhamento = alinhamento
        self.repouso = True
        self.imagem = pygame.image.load(f'sprits/{self.nome}_parado_esquerda_1.png')
        self.esquerda = {
            'parado': Animação(f'sprits/{self.nome}_parado_esquerda_', 7, (0, 0), 90),
            'correndo': Animação(f'sprits/{self.nome}_esquerda_', 12, (-2, 0), 30),
            'pulo': Animação(f'sprits/{self.nome}_pulo_esquerda_', 9, (0, -4), 30)
        }
        self.direita = {
            'parado': Animação(f'sprits/{self.nome}_parado_direita_', 7, (0, 0), 90),
            'correndo': Animação(f'sprits/{self.nome}_direita_', 12, (2, 0), 30),
            'pulo': Animação(f'sprits/{self.nome}_pulo_direita_', 9, (0, -4), 30)
        }


pygame.display.set_caption('Animação em pygame')
window = pygame.display.set_mode((1000, 400))

arial = pygame.font.SysFont('Arial', 10)
soldier = Personagem('Soldier')

fluides = 30
posX = 970
posY = 200
desloc = 2

while True:
    tempo = int(pygame.time.get_ticks())
    relogio = arial.render(f'Tempo: {tempo/100}', 0, (255, 255, 255))
    direção = arial.render(f'Alinhamento a {soldier.alinhamento}', 0, (255, 255, 255))
    coordX = arial.render(f'Eixo X: {posX}', 0, (255,255,255))
    coordY = arial.render(f'Eixo Y: {posY}', 0, (255,255,255))

    window.fill((0, 0, 0))
 
    if soldier.esquerda['correndo'].ativo and not soldier.esquerda['pulo'].ativo:
        soldier.imagem = soldier.esquerda["correndo"].on(tempo)

    elif soldier.direita['correndo'].ativo and not soldier.direita['pulo'].ativo:
        soldier.imagem = soldier.direita['correndo'].on(tempo)

    elif soldier.esquerda['pulo'].ativo:
        soldier.imagem = soldier.esquerda['pulo'].on(tempo, soldier)

    elif soldier.direita['pulo'].ativo:
        soldier.imagem = soldier.direita['pulo'].on(tempo, soldier)

    if soldier.repouso:
        if soldier.alinhamento == 'esquerda':
            soldier.imagem = soldier.esquerda["parado"].on(tempo)
        else:
            soldier.imagem = soldier.direita['parado'].on(tempo)
            

    pygame.draw.line(window, (20, 20, 20), (0, 243), (1000, 243), 4)
    
    window.blit(soldier.imagem, (posX, posY))
    window.blit(relogio, (10, 20))
    window.blit(direção, (10, 33))
    window.blit(coordX, (10, 46))
    window.blit(coordY, (10, 59))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:  # se uma tecla for precionada
            if event.key == K_a and not soldier.direita['correndo'].ativo:  # se a tecla for A e não D
                soldier.esquerda['correndo'].ativo = True
                
                soldier.repouso = False
                soldier.alinhamento = 'esquerda'

            elif event.key == K_d and not soldier.esquerda['correndo'].ativo:  # se a tecla for D e não A
                soldier.direita['correndo'].ativo = True

                soldier.repouso = False
                soldier.alinhamento = 'direita'

            elif event.key == K_w:
                if soldier.alinhamento == 'esquerda':
                    if not soldier.repouso:
                        soldier.esquerda['pulo'].X = -3
                        
                    soldier.esquerda['pulo'].ativo = True
                                
                else:
                    if not soldier.repouso:
                        soldier.direita['pulo'].X = 3

                    soldier.direita['pulo'].ativo = True

                soldier.repouso = False

        elif event.type == pygame.KEYUP:  # se uma tecla for solta
            if event.key == K_a and not soldier.direita['correndo'].ativo:
                soldier.esquerda['correndo'].ativo = False
                soldier.repouso = True

            elif event.key == K_d and not soldier.esquerda['correndo'].ativo:
                soldier.direita['correndo'].ativo = False
                soldier.repouso = True

    pygame.display.update()
