import pygame
import sys
import json

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WALLS = (255, 245, 204)
BROWN = (102, 68, 0)
YELLOW = (234, 237, 52)

from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')
pygame.draw.rect(screen, WHITE,)
while True:  # main game loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
sys.exit()
pygame.display.update()
screen = create_screen()
player = load_player_image()
background = load_background_image()
screen.blit(background, (0, 0))        #draw the background
position = player.get_rect()
screen.blit(player, position)          #draw the p000er
pygame.display.update()                #and show it all
for x in range(100):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(2, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(100)
