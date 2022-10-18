class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Cores como vsriáveis constantes
        GRAY = (230, 230, 230)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (160, 160, 0)
        VIOLET = (200, 0, 200)
        PINK = (255, 0, 255)

        # Configurações da tela
        self.ship_speed_factor = 1.5
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = GRAY

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = PINK
        self.bullets_allowerd = 3
