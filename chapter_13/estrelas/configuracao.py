class Configuracao():
    """Uma classe para armazenar todas as configurações da Strela."""
    def __init__(self):
        """Inicializa as configurações da tela."""

        # Cor
        BLUE = (0, 0, 255)
   
        # Configurações da tela
        self.titulo = "Estrela"
        self.tela_largura = 800
        self.tela_altura = 900
        self.tela_cor = BLUE
