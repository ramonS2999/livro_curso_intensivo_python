import pygame
import sys

from disparolateral.bala import Bala

def verifica_evento_keydown(evento, configuracao, tela, nave, balas):
    """Responde a pressionamento de tecla."""

    if evento.key == pygame.K_UP:
        # Move a espaçonave para a cima
        nave.move_cima = True
        
    elif evento.key == pygame.K_DOWN:
        # Move a espaçonave para a baixo
        nave.move_baixo = True
    
    elif evento.key == pygame.K_SPACE:
        disparar_bala(configuracao, tela, nave, balas)

def disparar_bala(configuracao, tela, nave, balas):
    """Dispara um projétio se o limite ainda não foi alcançado."""
    
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(balas) < configuracao.bala_quantidade:
        nova_bala = Bala(configuracao, tela, nave)
        balas.add(nova_bala)

def verifica_evento_keyup(evento, nave):
    if evento.key == pygame.K_UP:
        # Move a espaçonave para a cima
        nave.move_cima = False
        
    elif evento.key == pygame.K_DOWN:
        # Move a espaçonave para a baixo
        nave.move_baixo = False

def verifica_evento(configuracao, tela, nave, balas):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        
        elif evento.type == pygame.KEYDOWN:
            verifica_evento_keydown(evento, configuracao, tela, nave, balas)

        elif evento.type == pygame.KEYUP:
            verifica_evento_keyup(evento, nave)

def atualiza_tela(configuracao, tela, nave, balas):
    """Atualiza as imagens na tela e altera para a nova tela."""

    # Redesenha todos os projéteis atrás da espaçonave
    tela.fill(configuracao.tela_cor)
    for bala in balas.sprites():
        bala.desenhar_bala()
    nave.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def atualizar_bala(balas, configuracao):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""

    # Atualiza as posições dos projéteis
    balas.update()

    # Livra-se dos projéteis que desapareceram
    for bala in balas.copy():
        if bala.retangulo_bala.left >= configuracao.tela_largura:
            balas.remove(bala)
