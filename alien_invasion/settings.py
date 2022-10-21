class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Cores como vsriáveis constantes
        color = {
            "gray": (230, 230, 230),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (160, 160, 0),
            "violet": (200, 0, 200),
            "pink": (255, 0, 255),
        }

        # Configurações da tela
        self.ship_speed_factor = 1.5
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = color["gray"]

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = color["pink"]
        self.bullets_allowerd = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda 
        self.fleet_direction = 1
