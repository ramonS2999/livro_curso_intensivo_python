import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    # Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:
        gf.cheeck_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
