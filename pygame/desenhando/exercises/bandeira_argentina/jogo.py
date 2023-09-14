import pygame


def inicializa():
    pygame.init()
    window = pygame.display.set_mode((300, 200))
    pygame.display.set_caption("Bandeira da Argentina")

    # TODO: carregar imagem aqui e criar dicionário assets
    assets = {}
    assets['sol'] = pygame.image.load('sol.png')
    return window, assets


def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True


def desenha(window, assets):
    # TODO: desenhar a bandeira aqui
    window.fill((255, 255, 255))
    color = (116, 172, 223)
    pygame.draw.rect(window, color, pygame.Rect(0, 0, 300, 50 ))
    window.blit(assets['sol'], (100, 50))
    pygame.draw.rect(window, color, pygame.Rect(0, 150, 300, 200 ))
    pygame.display.update()


def game_loop(window, assets):
    # TODO: receber assets como argumento e repassar para desenha
    while recebe_eventos():
        desenha(window, assets)


if __name__ == '__main__':
    # TODO: receber assets aqui e repassar para game_loop
    w, assets = inicializa()
    game_loop(w, assets)

