# -*- coding: utf-8 -*-
# Copyright (C) 2018 3CP Studios.

print("\nStarting programme...\n\n. . .\n")

import pygame,numpy,random
from time import sleep as delay

pygame.init()

screen = pygame.display.set_mode((640,480)) # Screen size of game window

background = pygame.Surface(screen.get_size()) # Create empty pygame surface
background.fill((255,255,255))
background = background.convert() # Convering surface to make bitting faster

screen.blit(background, (0,0))

clock = pygame.time.Clock()

mainloop = True
FPS = 30
playtime = 0.0

while mainloop:
  miliseconds = clock.tick(FPS) # Don't go faster than this framerate
  playtime += miliseconds / 1000.0 # Add seconds to playtime
  
  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainloop = False # Pygame window closed by user
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        mainloop = False # User pressed ESC so close the program

  text = f"FPS: {clock.get_fps()}     Playtime: {playtime}"
  pygame.display.set_caption(text)
  
  pygame.display.flip()

pygame.quit()

print(f"Game played for {playtime} seconds.")
