import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial."""

        super().__init__()
        self.screen = screen
        self.ai_settigns = ai_settings

        # Carregar a imagem do alienígena e define o seu atributo rect
        self.image = pygame.image.load(".\\alien_invasion\\images\\alien.bmp")
        self.rect = self.image.get_rect()

        #Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Desenha o alienígena em sua posição atual."""

        self.screen.blit(self.image, self.rect)
