
import pygame

# SCALE AN IMAGE TO FIT THE SCREEN
 
pygame.init()
 
screen = pygame.display.set_mode((600, 500))
bg = pygame.image.load("image.png").convert_alpha()
sw, sh = screen.get_size()
while True:
    screen.blit(pygame.transform.scale(bg, (sw, sh)),(0, 0))
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()
pygame.quit()