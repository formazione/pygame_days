import pygame

# SCALE AN IMAGE TO FIT THE SCREEN
 
pygame.init()
 
def show(fit=0):
    ''' use show(1) to fit the screen '''
    screen = pygame.display.set_mode((600, 500))
    bg = pygame.image.load("image.png").convert_alpha()
    sw, sh = screen.get_size()
    if fit:
        screen.blit(pygame.transform.scale(bg, (sw, sh)),(0, 0))
    else:
        screen.blit(bg,(0, 0))
    while True:
        if pygame.event.get(pygame.QUIT):
            break
        pygame.display.update()
    pygame.quit()

show(1)