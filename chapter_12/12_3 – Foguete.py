print('''
            12.3 – Foguete: Crie um jogo que comece com um foguete no centro da tela.
            Permita que o jogador mova o foguete para cima, para baixo, para a direita e
            para a esquerda usando as quatro teclas de direção. Garanta que o foguete
            não se desloque para além de qualquer borda da tela.
''')
import pygame
from nave.configuracao import Configuracao
from nave.foguete import Foguete
import nave.funcao_jogo as funcao_jogo

def run_game():
    # Inicializa o pygame, as configurações e o objeto janela
    pygame.init()
    foguete_configuracao = Configuracao()
    janela = pygame.display.set_mode((foguete_configuracao.janela_largura, foguete_configuracao.janela_altura))
    pygame.display.set_caption(foguete_configuracao.titulo)

    # Cria uma espaçonave
    foguete = Foguete(foguete_configuracao, janela)

    # Inicia o laço principal do jogo
    while True:
        funcao_jogo.cheeck_events(foguete)
        foguete.update()
        funcao_jogo.update_janela(foguete_configuracao, janela, foguete)

run_game()