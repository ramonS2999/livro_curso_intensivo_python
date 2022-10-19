"""Importando o módolo pygame"""
import pygame

class Personagem():
    def __init__(self, tela):
            """Inicializa o personagem sua posição inicial"""
            self.tela = tela

            """Carregar a imagem do personagem e obtém seu retangulo"""
            self.image = pygame.image.load(".\\chapter_12\\personagem\\kisspng.bmp")
            self.retangulo = self.image.get_rect()

    def blitme(self):
        """Desenha o personagem em sua posição atual."""
        self.tela.blit(self.image, self.retangulo)