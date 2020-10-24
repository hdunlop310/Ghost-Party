import pygame, sys, random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode([1300, 600])

width = 1300
height = 600
colour = (49, 49, 49)
clock = pygame.time.Clock()
mixer.init()

# Loading the song
mixer.music.load("sounds/mastered maybe (Mastered with Thunder at 50pct).wav")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

white_ghost = pygame.image.load('ghosts/white ghost.png').convert_alpha()
white_ghost = pygame.transform.scale(white_ghost, (61, 82))

green_ghost = pygame.image.load('ghosts/green ghost.png').convert_alpha()
green_ghost = pygame.transform.scale(green_ghost, (61, 82))

orange_ghost = pygame.image.load('ghosts/orange ghost.png').convert_alpha()
orange_ghost = pygame.transform.scale(orange_ghost, (61, 82))

purple_ghost = pygame.image.load('ghosts/purple ghost.png').convert_alpha()
purple_ghost = pygame.transform.scale(purple_ghost, (61, 82))

ghost_pos = 0


# pos = 0:"white", 1:"green", 2:"orange", 3:"purple"
def ghost(pos):
    if pos == 0:
        screen.blit(white_ghost, (132, 503))
    if pos == 1:
        screen.blit(green_ghost, (427, 503))
    if pos == 2:
        screen.blit(orange_ghost, (780, 503))
    if pos == 3:
        screen.blit(purple_ghost, (1107, 503))


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
                # sets ghost_position
                ghost_pos = 0;

            if event.key == pygame.K_s:
                # sets ghost_position
                ghost_pos = 1;

            if event.key == pygame.K_d:
                # sets ghost_position
                ghost_pos = 2;

            if event.key == pygame.K_f:
                # sets ghost_position
                ghost_pos = 3;

            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_e:
                mixer.music.unpause()

    screen.fill(colour)
    pygame.draw.rect(screen, (255, 255, 255), [(0, 470), (350, 10)])
    pygame.draw.rect(screen, (82, 172, 0), [(350, 470), (350, 10)])
    pygame.draw.rect(screen, (242, 143, 28), [(650, 470), (350, 10)])
    pygame.draw.rect(screen, (110, 58, 158), [(950, 470), (350, 10)])
    ghost(ghost_pos)

    clock.tick(60)

    pygame.display.update()

pygame.quit()
