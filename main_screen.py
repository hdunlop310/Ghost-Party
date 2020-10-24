import pygame, sys, random
from pygame import mixer

from practice import white_ghost, green_ghost, orange_ghost, purple_ghost

pygame.init()

screen = pygame.display.set_mode([1300, 600])
width = 1300
height = 600
colour = (49, 49, 49)
button_colour = (255, 255, 255)
text_colour = (0, 0, 0)
clock = pygame.time.Clock()
mixer.init()


class Main_Screen():
    def handle_event(self, event):
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('Start', True, text_colour)

        button = pygame.Rect((int(width / 2), int(height / 2)), (100, 50))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                # prints current location of mouse
                print('button was pressed at {0}'.format(mouse_pos))
                scene.update('Game')

        screen.fill(colour)
        pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
        screen.blit(text, (int(width / 2) + 15, int(height / 2) + 5))

        pygame.display.update()

    def update(self, new_scene):
        return scenes[new_scene]


class Instructions_Screen():
    pass


class Game_Screen():
    def handle_event(self, event):
        # Loading the song
        mixer.music.load("sounds/mastered maybe (Mastered with Thunder at 50pct).wav")
        # Setting the volume
        mixer.music.set_volume(0.7)
        # Start playing the song
        mixer.music.play()
        white_ghost = pygame.image.load('ghosts/white ghost.png')
        green_ghost = pygame.image.load('ghosts/green ghost.png')
        orange_ghost = pygame.image.load('ghosts/orange ghost.png')
        purple_ghost = pygame.image.load('ghosts/purple ghost.png')

        ghostx = 30
        ghosty = 30

        # x = x-coords, y = y-coords, which_ghost = "white", "green", "orange", "purple"
        def ghost(x, y, which_ghost):
            if which_ghost == "white":
                screen.blit(white_ghost, (x, y))
            if which_ghost == "green":
                screen.blit(green_ghost, (x, y))
            if which_ghost == "orange":
                screen.blit(orange_ghost, (x, y))
            if which_ghost == "purple":
                screen.blit(purple_ghost, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_a:
                    print("player pressed a")
                    # change variable holding dimentions/colour
                    ghostx -= 10

                if event.key == pygame.K_d:
                    ghostx += 10
                    print("player pressed d")
                    # change variable holding dimentions/colour

                if event.key == pygame.K_p:
                    mixer.music.pause()
                if event.key == pygame.K_e:
                    mixer.music.unpause()

        screen.fill(colour)
        ghost(ghostx, ghosty, "orange")

        clock.tick(60)

        pygame.display.update()


scenes = {'Main': Main_Screen(),
          'Game': Game_Screen(),
          'Instructions': Instructions_Screen()}

scene = scenes['Main']

game_running = True
while game_running:
    for event in pygame.event.get():
        scene.handle_event(event)

pygame.quit()
