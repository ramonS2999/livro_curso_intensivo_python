class Configuracao():
    """Uma classe para armazenar todas as configurações da Navi Lateral."""

    def __init__(self):

        # Cores
        VERMELHO = (255, 0, 0)
        AZUL_BEBE = (0,255,255)

        # Configuração da tela
        self.velocidade_nave = 2.2
        self.tela_titulo = "Navi Lateral"
        self.tela_altua = 800
        self.tela_largura = 1200
        self.tela_cor = AZUL_BEBE

        # Configuração dos projéteis
        self.velocidade_bala = 1
        self.bala_largura = 20
        self.bala_altura = 10
        self.bala_cor = VERMELHO
        self.bala_cadencia = 5
