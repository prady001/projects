import pygame


def inicializa():
    pygame.init()
    win = pygame.display.set_mode((300, 200))
    pygame.display.set_caption("Bandeira da França")
    
    return win


def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    
    return True
    

def desenha(window):
    # TODO: desenhar a bandeira aqui
    pygame.draw.rect(window, (0,0, 255), pygame.Rect(0, 0, 100, 200))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(100, 0, 200, 200))
    pygame.draw.rect(window, (255,0, 0), pygame.Rect(200, 0, 300, 200))
    pygame.display.update()


def game_loop(window):
    while recebe_eventos():
        desenha(window)


if __name__ == '__main__':
    w = inicializa()
    game_loop(w)
