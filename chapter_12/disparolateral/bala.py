import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Uma classe que administra projéteis disparando pela espaçonave"""

    def __init__(self, configuracao, tela, nave):
        """Cria um objeto para o projétil atual da espaçonave."""

        super().__init__()
        self.tela = tela

        # Cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta
        self.retangulo_bala = pygame.Rect(0, 0, configuracao.bala_largura, configuracao.bala_altura)
        self.retangulo_bala.centery = nave.retangulo_nave.centery
        self.retangulo_bala.right = nave.retangulo_nave.right

        # Armazena a posição do projétil como um valor decimal
        self.x = float(self.retangulo_bala.x)

        self.cor = configuracao.bala_cor
        self.velocidade = configuracao.velocidade_bala
    
    def update(self):
        """Move o projétil para direita na tela."""

        # Atualiza a posição decimal do projétio
        self.x += self.velocidade

        # Atualiza a posição de rect
        self.retangulo_bala.x = self.x
    
    def desenhar_bala(self):
        """desenha o projétil na tela"""
        pygame.draw.rect(self.tela, self.cor, self.retangulo_bala)
