import sys
import pygame

from estrelas.estrela import Estrela

def verifica_evento():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def atualiza_tela(configuracao, tela, estrelas):
    """Atualiza as imagens na tela e altera para a nova tela."""

    tela.fill(configuracao.tela_cor)
    # Deixa a tela mais recente visível
    estrelas.draw(tela)
    pygame.display.flip()

def crear_constelacao(configuracao, tela, estrelas):
    """Cria uma constelação completa de esterela."""

    # Cria um estrelaígena e calcula o número de estrelaígenas em uma linha
    estrela = Estrela(configuracao, tela)
    number_estrelas_x = get_number_estrelas_x(configuracao, estrela.rect.width)
    numero_linha = get_numero_linha(configuracao, estrela.rect.height)

    # Cria a frota de estrelaígenas
    for numero_linha in range(numero_linha):
        for estrela_number in range(number_estrelas_x):
            crear_estrela(configuracao, tela, estrelas, estrela_number, numero_linha)
    
def get_number_estrelas_x(configuracao, estrela_largura):
    """Determina o número de estrelas que cabem em uma linha."""

    espaco_disponivel_x = configuracao.tela_largura - 2 * estrela_largura
    number_estrelas_x = int(espaco_disponivel_x / (estrela_largura))
    return number_estrelas_x

def crear_estrela(configuracao, tela, estrelas, estrela_number, numero_linha):

    # Cria uma estrela e o posiciona na linha
    estrela = Estrela(configuracao, tela)
    estrela_largura = estrela.rect.width
    estrela.x = estrela_largura + 2 * estrela_largura * estrela_number
    estrela.rect.x = estrela.x
    estrela.rect.y = estrela.rect.height + 2 * estrela.rect.height * numero_linha
    estrelas.add(estrela)

def get_numero_linha(configuracao, estrela_altura):
    """Determina o número de linha com estrelas que cabem na tela."""

    espaco_disponivel_y = (configuracao.tela_altura - (3 * estrela_altura))
    numero_linha = int(espaco_disponivel_y / (2 * estrela_altura))
    return numero_linha
