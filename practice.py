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
                ghostx += 10
                pygame.display.update()
            elif event.key == pygame.K_d:
                print("player pressed d")
                #change variable holding dimentions/colour
                pygame.display.update()
        ghost(ghostx, ghosty)
        pygame.display.update()

    screen.fill((colour))

    #pygame.draw.rect(screen, (0, 0, 255), [(30, 30), (30, 30)])
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
