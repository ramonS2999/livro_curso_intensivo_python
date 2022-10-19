import pygame

class Foguete():
    def __init__(self, foguete_configuracao, janela):
        self.janela = janela
        self.foguete_configuracao = foguete_configuracao

        # Carregar a imagem da espaçonave e obtém seu rect
        self.caminho = ".\\chapter_12\\nave\\ship.bmp"
        self.image = pygame.image.load(self.caminho)
        self.rect = self.image.get_rect()
        self.janela_rect = janela.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.janela_rect.centerx
        self.rect.bottom = self.janela_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.horizontal = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

        # flag de movimento
        self.move_direita = False
        self.move_esquerda = False
        self.move_cima = False
        self.move_baixo = False

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.move_direita and self.rect.right < self.janela_rect.right:
            self.horizontal += self.foguete_configuracao.fator_velocidade_foguete
            
        if self.move_esquerda and self.rect.left > 0:
            self.horizontal -= self.foguete_configuracao.fator_velocidade_foguete
        
        if self.move_cima and self.rect.top > 0:
            self.vertical -= self.foguete_configuracao.fator_velocidade_foguete
        
        if self.move_baixo and self.rect.bottom < self.janela_rect.bottom:
            self.vertical += self.foguete_configuracao.fator_velocidade_foguete
        
        # Atualiza o objeto rect de acordo com self.horizontal
        self.rect.centerx = self.horizontal
        self.rect.centery = self.vertical

    def blitme(self):
        """Desenha a espaçomave em sua posição atual."""
        self.janela.blit(self.image, self.rect)