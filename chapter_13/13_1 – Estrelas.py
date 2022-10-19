print('''
            13.1 – Estrelas: Encontre uma imagem de uma estrela. Faça uma grade de
            estrelas aparecer na tela.
''')

import pygame
from pygame.sprite import Group

from estrelas.configuracao import Configuracao
import estrelas.funcao as funcao

def play_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    configuracao = Configuracao()
    tela = pygame.display.set_mode((configuracao.tela_altura, configuracao.tela_largura))
    pygame.display.set_caption(configuracao.titulo)

    # Cria a frota de alienígenas
    estrelas = Group()
    funcao.crear_constelacao(configuracao, tela, estrelas)

    # Inicia o laço principal do jogo
    while True:
        funcao.verifica_evento()
        funcao.atualiza_tela(configuracao, tela, estrelas)

play_game()
