import pygame


pygame.init()
# ==================== the screen surface ===================
screen = pygame.display.set_mode((400, 400)) # window
width, height = screen.get_size()
clock = pygame.time.Clock()

# ============== the player (a little surface) ==============
square = pygame.Surface((20, 20))
square.fill((255, 0, 0))

w, h = 100, 100 # inital position of the player (square)
# directions
right, left, up, down = 0, 0, 0, 0
speed = 5
# Infinite loop ======== Game loop ========================
while True:
    if left and w > 0:
            w -= speed
    elif right and w < width - 20:
            w += speed
    elif up and h > 0:
        h -= speed
    elif down and h < width - 20:
        h += speed
    screen.fill(0) # clear screen
    screen.blit(square, (w, h))
    # close button
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        # key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right, left, up, down = 1, 0, 0, 0
            elif event.key == pygame.K_LEFT:
                right, left, up, down = 0, 1, 0, 0
            elif event.key == pygame.K_UP:
                right, left, up, down = 0, 0, 1, 0
            elif event.key == pygame.K_DOWN:
                right, left, up, down = 0, 0, 0, 1
        if event.type == pygame.KEYUP:
            right, left, up, down = 0, 0, 0, 0

    clock.tick(60)
    pygame.display.update()

pygame.quit()