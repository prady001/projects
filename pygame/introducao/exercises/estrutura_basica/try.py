import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((500, 400))
    window.fill((0, 0, 0))
    pygame.display.set_captation('First game')
    assets = {}
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    
def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window, assets):
    scaled_disaply = pygame.transform.scale_by(window, 1)
    window.blit(assets['nave'], (100, 100))