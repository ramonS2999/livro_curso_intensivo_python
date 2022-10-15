print('''
            12.4 – Teclas: Em um arquivo Pygame, crie uma tela vazia. No laço de eventos,
            exiba o atributo event.key sempre que o evento pygame.KEYDOWN for detectado.
            Execute o programa e pressione várias teclas para ver como o Pygame
            responde.
''')

import sys
import pygame

def window():
    pygame.init()

    width = 1200
    height = 200
    black = (0, 0, 0)
    yellow = (200, 200, 0)

    pygame.display.set_caption("KEY")
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.Font('freesansbold.ttf', 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            tecla = str(event)
            text = font.render(tecla, True, black, yellow)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
        screen.fill((yellow))
        screen.blit(text, textRect)
        pygame.display.update()

window()