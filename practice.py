import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode([1500, 1000])

width = 1500
height = 1000
colour = (49,49,49)

clock = pygame.time.Clock()
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
                pygame.draw.rect(screen, (255, 255, 255), [(50, 50), (30, 30)])
                pygame.display.update()
            elif event.key == pygame.K_d:
                print("player pressed d")
                pygame.draw.rect(screen, (0, 255, 255), [(50, 50), (30, 30)])
                pygame.display.update()

    screen.fill((colour))

    pygame.draw.rect(screen, (0, 0, 255), [(30, 30), (30, 30)])
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
