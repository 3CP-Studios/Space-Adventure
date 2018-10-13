# -*- coding: utf-8 -*-
# Copyright (C) 3CP Studios
print("\nStarting programme...\n\n. . .\n")
import threading
import pygame
from time import sleep as delay
import random
import numpy

pygame.init()

screen = pygame.display.set_mode((640,480)) # Screen size of game window

background = pygame.Surface(screen.get_size()) # Create empty pygame surface
background.fill((0,0,0))
background = background.convert() # Convering surface to make bitting faster

screen.blit(background, (0,0))

playerX,playerY = screen.get_size()
playerX=playerX/2
playerY=playerY/2+playerY/2.5

pygame.key.set_repeat(True)

clock = pygame.time.Clock()

mainloop = True
FPS = 30
playtime = 0.0

player = None

while mainloop:
  screen.blit(background,(0, 0))
  
  miliseconds = clock.tick(FPS) # Don't go faster than this framerate
  playtime += miliseconds / 1000.0 # Add seconds to playtime
  
  # Event handler
  #def input_game(playerX, playerY):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop = False # Pygame window closed by user
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        mainloop = False # User pressed ESC so close the program
      #elif event.key == pygame.K_w: playerY+=-5
      #elif event.key == pygame.K_s: playerY+=5
      #elif event.key == pygame.K_d: playerX+=5
      #elif event.key == pygame.K_a: playerX+=-5
    if pygame.key.get_pressed()[pygame.K_w]==1: playerY+=-5
    if pygame.key.get_pressed()[pygame.K_s]==1: playerY+=5
    if pygame.key.get_pressed()[pygame.K_d]==1: playerX+=5
    if pygame.key.get_pressed()[pygame.K_a]==1: playerX+=-5
  #t1 = threading.Thread(target=lambda: input_game(playerX, playerY))
  #t1.daemon=True
  #t1.start()
  
  text = f"FPS: {clock.get_fps()}     Playtime: {playtime}"
  pygame.display.set_caption(text)
   
  player = pygame.draw.circle(screen, (255, 28, 28), (round(playerX), round(playerY)), 3)
  
  pygame.display.flip()

pygame.quit()

print(f"Game played for {playtime} seconds.")
