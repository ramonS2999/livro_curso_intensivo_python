import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:
        gf.cheeck_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets) 
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
