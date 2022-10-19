print('''
            12.2 – Personagem do jogo: Encontre uma imagem de bitmap de um
            personagem de jogo que você goste ou converta uma imagem em um bitmap.
            Crie uma classe que desenhe o personagem no centro da tela e faça a cor de
            fundo da imagem coincidir com a cor de fundo da tela ou vice-versa.
''')

import sys
import pygame
from personagem.personagem import Personagem

def window():
    pygame.init()

    pygame.display.set_caption("Tela Azul")
    tela = pygame.display.set_mode((800, 820))
    personagem = Personagem(tela)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        tela.fill((180, 180, 0))
        personagem.blitme()
        pygame.display.update()

window()