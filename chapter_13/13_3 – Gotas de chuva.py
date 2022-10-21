print('''
            13.3 – Gotas de chuva: Encontre uma imagem de uma gota de chuva e crie
            uma grade de gotas. Faça as gotas de chuva caírem em direção à parte
            inferior da tela até desaparecerem.
''')

from math import fabs
import pygame
import sys



def chover(screen, ballrect, speed):

    if ballrect.bottom <= (screen.get_height() + ballrect.height):
        ballrect.centery += speed
    else:
        ballrect.centery = -50

def verifica_eveno():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def game():
    pygame.init()

    play_game = True

    size = width, height = 1080, 800
    gray = 0,128,0
    speed = 1

    screen = pygame.display.set_mode((size))

    ball = pygame.image.load("..\livro_curso_intensivo_python\\chapter_13\\gota.bmp")
    ball = pygame.transform.scale(ball, (50, 50))

    ballrect = ball.get_rect()

    while play_game:
        
        verifica_eveno()
        chover(screen, ballrect, speed)
        screen.fill(gray)
        screen.blit(ball, ballrect)
        pygame.display.flip()

game()