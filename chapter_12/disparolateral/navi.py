import pygame

class Navi():
    def __init__(self, configuracao, tela):
        """Inicializa a espaçonave e define sua posição inicial"""

        self.tela = tela
        self.configuracao = configuracao

        # Carregar a imagem da espaçonave e obtém seu rect
        self.path = ".\\chapter_12\\disparolateral\\espaconavi.bmp"
        self.imagem = pygame.image.load(self.path)
        self.retangulo_nave = self.imagem.get_rect()
        self.retangulo_tela = self.tela.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.retangulo_nave.centery = self.retangulo_tela.centery
        self.retangulo_nave.left = self.retangulo_tela.left

        # Armazena um valor decimal para o centro da espaçonave
        self.centro = float(self.retangulo_nave.centery)

        # flag de movimento
        self.move_cima = False
        self.move_baixo = False

    def atualizar(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.move_cima and self.retangulo_nave.top > 0:
            self.centro -= self.configuracao.velocidade_nave
        
        if self.move_baixo and self.retangulo_nave.bottom < self.retangulo_tela.bottom:
            self.centro += self.configuracao.velocidade_nave
        
        # Atualiza o objeto rect de acordo com self.center
        self.retangulo_nave.centery = self.centro
    
    def blitme(self):
        """Desenha a espaçomave em sua posição atual."""

        self.tela.blit(self.imagem, self.retangulo_nave)
