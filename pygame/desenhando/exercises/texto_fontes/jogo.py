import pygame


def inicializa():
    pygame.init()
    win = pygame.display.set_mode((300, 200))
    pygame.display.set_caption("Teste de fontes")

    # TODO: carregar fontes
    assets = {}
    fonte_padrao = pygame.font.get_default_font()
    assets['fonte_16'] = pygame.font.Font(fonte_padrao, 16)
    
    assets['fonte_24'] = pygame.font.Font(fonte_padrao, 24)
    

    return win, assets


def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True


def desenha(window, assets):
    window.fill((0,0,0))
    fonte_16 = assets['fonte_16'].render("Fonte tamanho 16", True, (255, 255, 255))
    fonte_24 = assets['fonte_24'].render("Fonte tamanho 24", True, (0, 0, 255))
    # TODO: desenhar textos na tela
    window.blit(fonte_16, (10, 20))
    window.blit(fonte_24, (10, 70))

    pygame.display.update()


def game_loop(window, assets):
    while recebe_eventos():
        desenha(window, assets)


if __name__ == '__main__':
    window, assets = inicializa()
    game_loop(window, assets)
