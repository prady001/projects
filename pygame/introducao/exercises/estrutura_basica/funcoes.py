import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((320, 240))
    pygame.display.set_caption('Jogo do Prady')
    return  window

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True