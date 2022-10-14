print('''
            12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo azul.
''')

import sys
import pygame

def window():
    pygame.init()

    width = 800
    height = 500
    green = (0, 255, 0)
    blue = (0, 0, 128)

    pygame.display.set_caption("Tela Azul")
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('12.1 – Céu azul: Crie uma janela do Pygame com uma cor de fundo azul.', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((blue))
        screen.blit(text, textRect)
        pygame.display.update()

window()
