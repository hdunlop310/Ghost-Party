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
        print("game")


scenes = {'Main': Main_Screen(),
          'Game': Game_Screen(),
          'Instructions': Instructions_Screen()}

scene = scenes['Main']

game_running = True
while game_running:
    for event in pygame.event.get():
        scene.handle_event(event)

pygame.quit()
