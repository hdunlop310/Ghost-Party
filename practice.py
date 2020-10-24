import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode([1300, 600])

width = 1300
height = 600
colour = (49,49,49)
clock = pygame.time.Clock()
music = 'sounds/mastered maybe (Mastered with Thunder at 50pct).wav'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
pygame.event.wait()
player_white = pygame.image.load('ghosts/white ghost.png')

white_ghost = pygame.image.load('ghosts/white ghost.png')
green_ghost = pygame.image.load('ghosts/green ghost.png')
orange_ghost = pygame.image.load('ghosts/orange ghost.png')
purple_ghost = pygame.image.load('ghosts/purple ghost.png')

ghostx = 30
ghosty = 30

#x = x-coords, y = y-coords, which_ghost = "white", "green", "orange", "purple"
def ghost(x, y, which_ghost):
    if(which_ghost == "white"):
        screen.blit(white_ghost, (x, y))
    if(which_ghost == "green"):
        screen.blit(green_ghost, (x, y))
    if(which_ghost == "orange"):
        screen.blit(orange_ghost, (x, y))
    if(which_ghost == "purple"):
        screen.blit(purple_ghost, (x, y))

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
                
            if event.key == pygame.K_a:
                print("player pressed a")
                #change variable holding dimentions/colour
                ghostx -= 10
                
            if event.key == pygame.K_d:
                ghostx += 10
                print("player pressed d")
                #change variable holding dimentions/colour

    screen.fill(colour)
    ghost(ghostx, ghosty, "orange")

    clock.tick(60)

    pygame.display.update()

pygame.quit()
