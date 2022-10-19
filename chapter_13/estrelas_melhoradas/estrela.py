import pygame
from pygame.sprite import Sprite

class Estrela(Sprite):
    """Uma classe que representa uma única estrela da constelação."""

    def __init__(self, configuracao, tela):
        """Inicializa o alienígena e define sua posição inicial."""

        super().__init__()
        self.tela = tela
        self.configuracao = configuracao

        # Carregar a imagem da estrela e define o seu atributo rect
        self.image = pygame.image.load(".\\\chapter_13\\estrelas\\star.bmp")
        self.rect = self.image.get_rect()

        #Inicia cada nova estrela próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da estrela
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Desenha a estrela em sua posição atual."""

        self.tela.blit(self.image, self.rect)
