from re import X
from tkinter import W
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
        global tecla, superficie

        if tempo%self.fluides == 0:
            self.frame += 1
            
            # se o frame for igual a quantidade de quadros e ouver deslocação vertical
            if self.frame == self.quadros and self.Y:  
                self.ativo = False
                tecla['W'] = False
                self.frame = 1
                
                if self.X == 0:
                    sujeito.repouso = True
                else:
                    self.X = 0

            # se o frame for maior que a quantidade de quadros
            elif self.frame > self.quadros:
                if tecla['Q']:
                    self.frame = 3
                else:
                    if sujeito.ocupado:
                        self.ativo = False
                        sujeito.ocupado = False
                        sujeito.repouso = True
                    
                    self.frame = 1
                
            sujeito.X += self.X
            sujeito.caixa.left += self.X
            
            # para deslocar o personagem verticalmente com pulo e queda
            if self.frame <= self.quadros//2:
                sujeito.Y += self.Y 
                sujeito.caixa.top += self.Y                 
                
            elif self.quadros > self.frame > self.quadros//2:
                sujeito.Y += (self.Y - (self.Y + self.Y))
                sujeito.caixa.top += (self.Y - (self.Y + self.Y))
            
        quadro = arial.render(f'Frame: {self.frame}', 0, (255, 255, 255))
        superficie.blit(quadro, (10, 282))

        return pygame.image.load(f'{self.imagem}{self.frame}.png')


class Personagem:
    def __init__(self, nome, coordenada, alinhamento='esquerda'):
        self.nome = nome
        self.X = coordenada[0]
        self.Y = coordenada[1]
        self.alinhamento = alinhamento
        self.repouso = True
        self.ocupado = False
        self.imagem = pygame.image.load(f'sprits/{self.nome}_parado_esquerda_1.png')
        self.caixa = pygame.Rect(self.X, self.Y, self.imagem.get_width(), self.imagem.get_height())
        self.esquerda = dict()
        self.direita = dict()

        
    def animar(self, correr=False, pular=False, apontar=False):
        global tecla

        if correr and not self.ocupado:
            if self.esquerda['correndo'].ativo and not tecla['W']:
                self.imagem = self.esquerda["correndo"].on(tempo, self)

            elif self.direita['correndo'].ativo and not tecla['W']:
                self.imagem = self.direita['correndo'].on(tempo, self)

        if pular:
            if self.esquerda['pulo'].ativo:
                self.imagem = self.esquerda['pulo'].on(tempo, self)

            elif self.direita['pulo'].ativo:
                self.imagem = self.direita['pulo'].on(tempo, self)

        if apontar:
            if self.esquerda['apontando'].ativo:
                self.imagem = self.esquerda['apontando'].on(tempo, self)
            
            elif self.direita['apontando'].ativo:
                self.imagem = self.direita['apontando'].on(tempo, self)

            if self.esquerda['disparando'].ativo:
                self.imagem = self.esquerda['disparando'].on(tempo, self)
            
            elif self.direita['disparando'].ativo:
                self.imagem = self.direita['disparando'].on(tempo, self)

        if self.repouso:
            if self.alinhamento == 'esquerda':
                self.imagem = self.esquerda["parado"].on(tempo, self)
            else:
                self.imagem = self.direita['parado'].on(tempo, self)


pygame.display.set_caption('Animação em pygame')
window = pygame.display.set_mode((1000, 400))
superficie = pygame.Surface((1000, 400))

transparencia = pygame.Color(0, 0, 0, 0)
arial = pygame.font.SysFont('Arial', 10)
soldier = Personagem('Soldier', (970, 170))
rifleman = Personagem('Rifleman', (500, 161))
tecla = {
    'A': False,
    'D': False,
    'W': False,
    'Q': False
}
  # ============================================|Animações para o rifleman alinhado a esquerda|============================================
rifleman.esquerda['parado'] = Animação(f'sprits/{rifleman.nome}_parado_esquerda_', 4, (0, 0), 20)
rifleman.esquerda['correndo'] = Animação(f'sprits/{rifleman.nome}_esquerda_', 12, (-3, 0), 4)
rifleman.esquerda['apontando'] = Animação(f'sprits/{rifleman.nome}_apontando_esquerda_', 3, (0, 0), 20)
rifleman.esquerda['disparando'] = Animação(f'sprits/{rifleman.nome}_disparo_esquerda_', 17, (0, 0), 8)
rifleman.esquerda['pulo'] = False

  # ============================================|Animações para o rifleman alinhado a direita|============================================
rifleman.direita['parado'] = Animação(f'sprits/{rifleman.nome}_parado_direita_', 4, (0, 0), 20)
rifleman.direita['correndo'] = Animação(f'sprits/{rifleman.nome}_direita_', 12, (3, 0), 4)
rifleman.direita['apontando'] = Animação(f'sprits/{rifleman.nome}_apontando_direita_', 3, (0, 0),20)
rifleman.direita['disparando'] = Animação(f'sprits/{rifleman.nome}_disparo_direita_', 17, (0, 0), 8)
rifleman.direita['pulo'] = False
 
  # ============================================|Animações para o soldier alinhado a esquerda|============================================
soldier.esquerda['parado'] = Animação(f'sprits/{soldier.nome}_parado_esquerda_', 7, (0, 0), 20)
soldier.esquerda['correndo'] = Animação(f'sprits/{soldier.nome}_esquerda_', 12, (-2, 0), 4)
soldier.esquerda['apontando'] = False
soldier.esquerda['pulo'] = Animação(f'sprits/{soldier.nome}_pulo_esquerda_', 9, (0, -4), 6)

  # ============================================|Animações para o soldier alinhado a direita|============================================
soldier.direita['parado'] = Animação(f'sprits/{soldier.nome}_parado_direita_', 7, (0, 0), 20)
soldier.direita['correndo'] = Animação(f'sprits/{soldier.nome}_direita_', 12, (2, 0), 4)
soldier.direita['apontando'] = False
soldier.direita['pulo'] = Animação(f'sprits/{soldier.nome}_pulo_direita_', 9, (0, -4), 6)

controle = soldier
while True:
    tempo = int(pygame.time.get_ticks())
    relogio = arial.render(f'Tempo: {tempo/100}', 0, (255, 255, 255))
    direção = arial.render(f'Alinhamento a {controle.alinhamento}', 0, (255, 255, 255))
    coordX = arial.render(f'Eixo X: {controle.X}', 0, (255,255,255))
    coordY = arial.render(f'Eixo Y: {controle.Y}', 0, (255,255,255))
    seleção = arial.render(f'Personagem: {controle.nome}', 0, (255, 255, 255))

    soldier.animar(correr=True, pular=True)
    rifleman.animar(correr=True, apontar=True)
            
    window.blit(superficie, (0, 0))
  
    pygame.draw.rect(superficie, transparencia, soldier.caixa)
    pygame.draw.rect(superficie, transparencia, rifleman.caixa)

    superficie.blit(pygame.image.load('sprits/Fundo_1.png'), (0, 0))
    
    superficie.blit(rifleman.imagem, (rifleman.X, rifleman.Y))
    superficie.blit(soldier.imagem, (soldier.X, soldier.Y))
    superficie.blit(pygame.image.load('sprits/Arvore_1.png'), (435, 0))

    window.blit(relogio, (10, 230))
    window.blit(direção, (10, 243))
    window.blit(coordX, (10, 256))
    window.blit(coordY, (10, 269))
    window.blit(seleção, (10, 292))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

  # ===================================================|Se uma tecla for precionada|=================================================== 
        elif event.type == pygame.KEYDOWN:  
        
            # se a tecla for A
            if event.key == K_a and not tecla['D'] and not tecla['W'] and not tecla['Q'] and not controle.ocupado:
                tecla['A'] = True
                controle.esquerda['correndo'].ativo = True
                
                controle.repouso = False
                controle.alinhamento = 'esquerda'

            # se a tecla for D
            elif event.key == K_d and not tecla['A'] and not tecla['W'] and not tecla['Q'] and not controle.ocupado:  
                tecla['D'] = True
                controle.direita['correndo'].ativo = True

                controle.repouso = False
                controle.alinhamento = 'direita'

            # se a tecla for W
            elif event.key == K_w and controle.esquerda['pulo'] and not controle.ocupado:
                tecla['W'] = True

                if controle.alinhamento == 'esquerda':
                    if controle.esquerda['pulo'] and not controle.repouso:
                        controle.esquerda['pulo'].X = -3
                        
                    controle.esquerda['pulo'].ativo = True
                                
                else:
                    if not controle.repouso:
                        controle.direita['pulo'].X = 3

                    controle.direita['pulo'].ativo = True

                controle.repouso = False
            
            # se a tecla for o shift esquerdo
            elif event.key == K_q and controle.esquerda['apontando'] and not tecla['W']:
                if controle.alinhamento == 'esquerda':
                    controle.esquerda['apontando'].ativo = True
                    if tecla['A']:
                        controle.esquerda['correndo'].ativo = False

                else:
                    controle.direita['apontando'].ativo = True
                    if tecla['D']:
                        controle.direita['correndo'].ativo = False

                tecla['Q'] = True
                controle.repouso = False

            elif event.key == K_e and tecla['Q']:
                if controle.alinhamento == 'esquerda':
                    controle.esquerda['disparando'].ativo = True
                    controle.esquerda['apontando'].ativo = False
                else:
                    controle.direita['disparando'].ativo = True
                    controle.direita['apontando'].ativo = False
                
                controle.ocupado = True
                tecla['Q'] = False

  # =====================================================|Se uma tecla for solta|=======================================================
        elif event.type == pygame.KEYUP:  
            if event.key == K_a and not controle.direita['correndo'].ativo and not tecla['Q']:
                tecla['A'] = False
                controle.esquerda['correndo'].ativo = False
                controle.repouso = True

            elif event.key == K_d and not controle.esquerda['correndo'].ativo and not tecla['Q']:
                tecla['D'] = False
                controle.direita['correndo'].ativo = False
                controle.repouso = True

            elif event.key == K_q and controle.esquerda['apontando'] and tecla['Q']:
                controle.esquerda['apontando'].ativo = False
                controle.direita['apontando'].ativo = False
                tecla['Q'] = False
                controle.repouso = True

  # ==============================================|Se o botão do mouse for presionado|==============================================
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if soldier.caixa.collidepoint(pygame.mouse.get_pos()):
                controle = soldier

            elif rifleman.caixa.collidepoint(pygame.mouse.get_pos()):
                controle = rifleman

    pygame.display.update()
