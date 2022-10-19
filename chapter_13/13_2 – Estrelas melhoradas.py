print('''
            113.2 – Estrelas melhoradas: Você pode criar um padrão mais realista de estrelas
            introduzindo uma aleatoriedade ao posicionar cada estrela. Lembre-se de que
            um número aleatório pode ser obtido assim: from random import randint
            random_number = randint(-10,10) Esse código devolve um inteiro
            aleatório entre −10 e 10. Usando o seu código do Exercício 13.1, ajuste
            a posição de cada estrela de acordo com um valor aleatório.
''')

import pygame
from pygame.sprite import Group

from estrelas_melhoradas.configuracao import Configuracao
import estrelas_melhoradas.funcao as funcao

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
