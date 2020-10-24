import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode([1300, 600])

width = 1300
height = 600
colour = (49,49,49)
clock = pygame.time.Clock()

ghost_image = pygame.image.load('ghost.png')
ghostx = 30
ghosty = 30

def ghost(x, y):
    screen.blit(ghost_image, (x, y))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_a:
                print("player pressed a")
                #change variable holding dimentions/colour
                ghostx -= 10
            elif event.key == pygame.K_d:
                ghostx += 10
                print("player pressed d")
                #change variable holding dimentions/colour

    screen.fill(colour)
    ghost(ghostx, ghosty)

    clock.tick(60)

    pygame.display.update()

pygame.quit()
