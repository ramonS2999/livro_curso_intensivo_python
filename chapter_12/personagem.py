"""Importando o módolo pygame"""
import pygame

class Personagem():
    def __init__(self, screen):
            """Inicializa o personagem sua posição inicial"""
            self.screen = screen

            """Carregar a imagem do personagem e obtém seu rect"""
            path = ".\\kisspng.bmp"
            self.image = pygame.image.load(path)
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()

            """Inicia cada nova espaçonave na parte inferior central da tela"""
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha o personagem em sua posição atual."""
        self.screen.blit(self.image, self.rect)