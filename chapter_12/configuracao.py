class Configuracao():
    """Uma classe para armazenar todas as configurações do Foguete Maroto."""
    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Cores
        self.cinza = (230, 230, 230)
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.vermelho = (255, 0, 0)
        self.verde = (0, 255, 0)
        self.azul = (0, 0, 255)
        self.amarelo = (255, 255, 0)

        # Configurações da tela
        self.fator_velocidade_foguete = 1.5
        self.titulo = "Foguete Maroto"
        self.janela_largura = 1200
        self.janela_altura = 800
        self.cor_fundo = self.cinza