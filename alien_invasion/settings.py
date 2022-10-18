class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Cores
        self.gray = (230, 230, 230)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (160, 160, 0)
        self.violet = (200, 0, 200)
        self.pink = (255, 0, 255)

        # Configurações da tela
        self.ship_speed_factor = 1.5
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self.gray

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = self.pink
