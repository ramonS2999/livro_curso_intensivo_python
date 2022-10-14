import pygame

class Ship():
    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = screen

        # Carregar a imagem da espaçonave e obtém seu rect
        path = ".\\alien_invasion\\images\\ship.bmp"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçomave em sua posição atual."""
        self.screen.blit(self.image, self.rect)