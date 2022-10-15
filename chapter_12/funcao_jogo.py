import sys
import pygame

def check_keydown_events(event, foguete):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        foguete.move_direita = True

    elif event.key == pygame.K_LEFT:
        # Move a espaçonave para a esquerda
        foguete.move_esquerda = True
    
    elif event.key == pygame.K_UP:
        foguete.move_cima = True
    
    elif event.key == pygame.K_DOWN:
        foguete.move_baixo = True

def check_keyup_events(event, foguete):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        foguete.move_direita = False
    
    elif event.key == pygame.K_LEFT:
        foguete.move_esquerda = False
    
    elif event.key == pygame.K_UP:
        foguete.move_cima = False
    
    elif event.key == pygame.K_DOWN:
        foguete.move_baixo = False

def cheeck_events(foguete):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, foguete)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, foguete)

def update_janela(foguete_configuracao, janela, foguete):
    """Atualiza as imagens na tela e altera para a nova tela."""
    
    # Redesenha a tela a cada passagem pelo laço
    janela.fill(foguete_configuracao.cor_fundo)
    foguete.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()