import pygame, sys, random
from datetime import datetime, time
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

start = datetime.now()
last_second = 0

guy1 = None

#fontface
white = (255,255,255)
font = pygame.font.SysFont("agencyfb", 60, True)


# pos = 0:"white", 1:"green", 2:"orange", 3:"purple"
def ghost(pos):
    if pos == 0:
        screen.blit(white_ghost, (132, 503))
    if pos == 1:
        screen.blit(green_ghost, (455, 503))
    if pos == 2:
        screen.blit(orange_ghost, (780, 503))
    if pos == 3:
        screen.blit(purple_ghost, (1107, 503))


def guyGenerate(which_guy):
    if which_guy == 0:
        white_guy = pygame.image.load('ghosts/white ghost.png').convert_alpha()
        white_guy = pygame.transform.scale(white_guy, (61, 82))
        return white_guy
    if which_guy == 1:
        green_guy = pygame.image.load('ghosts/green ghost.png').convert_alpha()
        green_guy = pygame.transform.scale(green_guy, (61, 82))
        return green_guy
    if which_guy == 2:
        orange_guy = pygame.image.load('ghosts/orange ghost.png').convert_alpha()
        orange_guy = pygame.transform.scale(orange_guy, (61, 82))
        return orange_guy
    if which_guy == 3:
        purple_guy = pygame.image.load('ghosts/purple ghost.png').convert_alpha()
        purple_guy = pygame.transform.scale(purple_guy, (61, 82))
        return purple_guy


orange_ghost = pygame.image.load('ghosts/orange ghost.png').convert_alpha()
orange_ghost = pygame.transform.scale(orange_ghost, (61, 82))

purple_ghost = pygame.image.load('ghosts/purple ghost.png').convert_alpha()
purple_ghost = pygame.transform.scale(purple_ghost, (61, 82))

move = False
pos = None
random_guy = 0
score = 0
got_point = False

end = False
game_running = True
while game_running:

    timer = str(datetime.now() - start)
    seconds = int(timer[5:7])
    minutes = int(timer[3])
    if minutes == 0:
        timer = seconds
    if minutes == 1:
        timer = seconds + 60
    if minutes == 2:
        timer = seconds + 120

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
    pygame.draw.rect(screen, (255, 255, 255), [(0, 470), (325, 10)])
    pygame.draw.rect(screen, (82, 172, 0), [(325, 470), (325, 10)])
    pygame.draw.rect(screen, (242, 143, 28), [(650, 470), (325, 10)])
    pygame.draw.rect(screen, (110, 58, 158), [(975, 470), (325, 10)])
    
    ghost(ghost_pos)

    if last_second != timer:
        move = False
        random_guy = random.randint(0, 3)
        guy1 = guyGenerate(random_guy)
        got_point = False
        last_second = timer
    if (guy1 != None) and (move == False):
        if random_guy == 0:
            pos = (132, -42)
        if random_guy == 1:
            pos = (455, -42)
        if random_guy == 2:
            pos = (780, -42)
        if random_guy == 3:
            pos = (1107, -42)
        screen.blit(guy1, pos)
        move = True
    if (guy1 != None) and (move == True):
        y = pos[1]
        y += 15
        pos = (pos[0], y)
        screen.blit(guy1, pos)
        
    if pos != None:
        if (pos[1] > 470 and pos[1] < 600 and got_point == False):
            if ghost_pos == random_guy:
                score += 1
                got_point = True

    playerScore = font.render(str(score), True, white)
    screen.blit(playerScore,(630,0))
    clock.tick(60)
    pygame.display.update()

    if timer == 122:
        game_running = False


pygame.quit()
