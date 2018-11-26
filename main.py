import pygame
import sys
import json

from pygame.locals import *

with open('static_data.json') as f:
    static_data = json.load(f)
colors = static_data["colors"]
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')
pygame.draw.rect(screen, colors["GREEN"], [100, 150, 200, 250])
pygame.display.update()
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
