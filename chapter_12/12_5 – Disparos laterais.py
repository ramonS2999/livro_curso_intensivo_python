print('''
            12.5 – Disparos laterais: Escreva um jogo que posicione uma espaçonave do
            lado esquerdo da tela e permita que o jogador a desloque para cima e para
            baixo. Faça a espaçonave disparar um projétil que se move para a direita da
            tela quando o jogador pressionar a barra de espaço. Garanta que os projéteis
            sejam apagados quando desaparecerem da tela.
''')

import pygame
from pygame.sprite import Group

from disparolateral.configuracao import Configuracao
from disparolateral.navi import Navi
import disparolateral.funcoes as funcao

def play_game():
    # Inicializa o pygame, as configurações e o objeto tela
    pygame.init()

    configuracao = Configuracao() 
    pygame.display.set_caption(configuracao.tela_titulo)
    tela = pygame.display.set_mode((configuracao.tela_largura, configuracao.tela_altua))

    # Cria uma espaçonave
    nave = Navi(configuracao, tela)

    # Cria um grupo no qual serão armazenados os projéteis
    balas = Group()

    # Inicia o laço principal do jogo
    while True:
        funcao.verifica_evento(configuracao, tela, nave, balas)
        nave.atualizar()
        funcao.atualizar_bala(balas, configuracao)
        funcao.atualiza_tela(configuracao, tela, nave, balas)

play_game()
