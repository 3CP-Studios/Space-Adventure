# -*- coding: utf-8 -*-

import Game_lib.game
import threading
import pygame
from time import sleep as delay
import random
import numpy
from PIL import Image

default_speed=12

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

speed = default_speed

bg_speed = 30 #FPS

pygame.init()
pygame.font.init()
pygame.event.set_blocked(pygame.MOUSEMOTION)

pygame.display.set_caption("Space Adventure")

class Anim(object):
  """A class to simplify the act of adding animations to sprites."""
  def __init__(self, frames, fps, loops=-1):
    """
    The argument frames is a list of frames in the correct order;
    fps is the frames per second of the animation;
    loops is the number of times the animation will loop (a value of -1
    will loop indefinitely).
    """
    self.frames = frames
    self.fps = fps
    self.frame = 0
    self.timer = None
    self.loops = loops
    self.loop_count = 0
    self.done = False

  def get_next_frame(self, now):
    """
    Advance the frame if enough time has elapsed and the animation has
    not finished looping.
    """
    if not self.timer:
      self.timer = now
    if not self.done and now-self.timer > 1000.0/self.fps:
      self.frame = (self.frame+1)%len(self.frames)
      if not self.frame:
        self.loop_count += 1
        if self.loops != -1 and self.loop_count >= self.loops:
          self.done = True
          self.frame -= 1
      self.timer = now
    return self.frames[self.frame]

  def reset(self):
    """Set frame, timer, and loop status back to the initialized state."""
    self.frame = 0
    self.timer = None
    self.loop_count = 0
    self.done = False

myFont=pygame.font.SysFont('Comic Sans MS', 20)

screen = pygame.display.set_mode((1280, 720)) # Screen size of game window. Also thankz Clorox for the idea of 720p

background = pygame.Surface(screen.get_size()) # Create empty pygame surface
background.fill((0,0,0))
background = background.convert() # Convering surface to make bitting faster

# Creating ship
ship1=pygame.image.load("Sprites/ship1.png")
ship2=pygame.image.load("Sprites/ship2.png")
ship3=pygame.image.load("Sprites/ship3.png")
shipimage=Anim([ship1,ship2,ship3], 10, -1)

# Creating star
star1=pygame.image.load("Sprites/star1.png")
star2=pygame.image.load("Sprites/star2.png")
star3=pygame.image.load("Sprites/star3.png")
star4=pygame.image.load("Sprites/star4.png")
star5=pygame.image.load("Sprites/star5.png")
star6=pygame.image.load("Sprites/star6.png")
star7=pygame.image.load("Sprites/star7.png")
star8=pygame.image.load("Sprites/star8.png")
star9=pygame.image.load("Sprites/star9.png")
star10=pygame.image.load("Sprites/star10.png")
star11=pygame.image.load("Sprites/star11.png")
star12=pygame.image.load("Sprites/star12.png")
star13=pygame.image.load("Sprites/star13.png")
star14=pygame.image.load("Sprites/star14.png")
star15=pygame.image.load("Sprites/star15.png")
star16=pygame.image.load("Sprites/star16.png")
star=Anim([star1,star2,star3,star4,star5,star6,star7,star8,star9,star10,star11,star12,star13,star14,star15,star16], 5, -1)

# Creating bg
bg0=pygame.image.load("Sprites/bg/frame_0_delay-0.1s.png")
bg1=pygame.image.load("Sprites/bg/frame_1_delay-0.1s.png")
bg2=pygame.image.load("Sprites/bg/frame_2_delay-0.1s.png")
bg3=pygame.image.load("Sprites/bg/frame_3_delay-0.1s.png")
bg4=pygame.image.load("Sprites/bg/frame_4_delay-0.1s.png")
bg5=pygame.image.load("Sprites/bg/frame_5_delay-0.1s.png")
bg6=pygame.image.load("Sprites/bg/frame_6_delay-0.1s.png")
bg7=pygame.image.load("Sprites/bg/frame_7_delay-0.1s.png")
bg8=pygame.image.load("Sprites/bg/frame_8_delay-0.1s.png")
bg9=pygame.image.load("Sprites/bg/frame_9_delay-0.1s.png")
bg10=pygame.image.load("Sprites/bg/frame_10_delay-0.1s.png")
bg11=pygame.image.load("Sprites/bg/frame_11_delay-0.1s.png")
bg12=pygame.image.load("Sprites/bg/frame_12_delay-0.1s.png")
bg13=pygame.image.load("Sprites/bg/frame_13_delay-0.1s.png")
bg14=pygame.image.load("Sprites/bg/frame_14_delay-0.1s.png")
bg15=pygame.image.load("Sprites/bg/frame_15_delay-0.1s.png")
bg16=pygame.image.load("Sprites/bg/frame_16_delay-0.1s.png")
bg17=pygame.image.load("Sprites/bg/frame_17_delay-0.1s.png")
bg18=pygame.image.load("Sprites/bg/frame_18_delay-0.1s.png")
bg19=pygame.image.load("Sprites/bg/frame_19_delay-0.1s.png")
bg20=pygame.image.load("Sprites/bg/frame_20_delay-0.1s.png")
bg21=pygame.image.load("Sprites/bg/frame_21_delay-0.1s.png")
bg22=pygame.image.load("Sprites/bg/frame_22_delay-0.1s.png")
bg23=pygame.image.load("Sprites/bg/frame_23_delay-0.1s.png")
bg24=pygame.image.load("Sprites/bg/frame_24_delay-0.1s.png")
bg25=pygame.image.load("Sprites/bg/frame_25_delay-0.1s.png")
bg26=pygame.image.load("Sprites/bg/frame_26_delay-0.1s.png")
bg27=pygame.image.load("Sprites/bg/frame_27_delay-0.1s.png")
bg28=pygame.image.load("Sprites/bg/frame_28_delay-0.1s.png")
bg29=pygame.image.load("Sprites/bg/frame_29_delay-0.1s.png")
bg30=pygame.image.load("Sprites/bg/frame_30_delay-0.1s.png")
bg31=pygame.image.load("Sprites/bg/frame_31_delay-0.1s.png")
bg32=pygame.image.load("Sprites/bg/frame_32_delay-0.1s.png")
bg=Anim([bg0,bg1,bg2,bg3,bg4,bg5,bg6,bg7,bg8,bg9,bg10,bg11,bg12,bg13,bg14,bg15,bg16,bg17,bg18,bg19,bg20,bg21,bg22,bg23,bg24,bg25,bg26,bg27,bg28,bg29,bg30,bg31,bg32], bg_speed)

screen.blit(background, (0,0))

playerX,playerY = screen.get_size()
playerX=playerX/2
playerY=playerY/2+playerY/2.5

pygame.key.set_repeat(True)

clock = pygame.time.Clock()

mainloop = True
FPS = 30
playtime = 0.0

class Bullet(pygame.sprite.Sprite):
  """ This class represents the bullet . """
  def __init__(self, pos, x, y):
    # Call the parent class (Sprite) constructor
    super().__init__()
    self.x,self.y=x,y
    self.image = pygame.Surface([4, 10])
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y=pos[0]-2,pos[1]-10
  def update(self):
    """ Move the bullet. """
    self.rect.y -= self.y
    self.rect.x += self.x

debug = False

player = None
clock = pygame.time.Clock()

bullet_list=pygame.sprite.Group()

# Importing Game_Lib
game_lib=Game_lib.game.game(screen, pygame.display)
game_lib.shoot((playerX, playerY), 10, Game_lib.game.DOWN)

while mainloop:
  all_sprites=pygame.sprite.Group()
  
  # "Clearing" screen
  #screen.blit(background,(0, 0))
  screen.fill((0,0,0))
  
  screen.blit(pygame.transform.scale(bg.get_next_frame(pygame.time.get_ticks()), (597, 846)),(0, 0))
  screen.blit(pygame.transform.scale(bg.get_next_frame(pygame.time.get_ticks()), (597, 846)),(round(screen.get_size()[0]/2), 0))
  
  # Big mess because of Star implementation fail
  #starz=pygame.sprite.Group(
  #Star(
    #(random.randint(0, screen.get_size()[0]), 1),
    #screen,
    #[]
    #star.get_next_frame(pygame.time.get_ticks()
  #))
  
  # The in-game clock
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
      elif event.key == pygame.K_m:
        debug = not debug
      #elif event.key == pygame.K_w: playerY+=-5
      #elif event.key == pygame.K_s: playerY+=5
      #elif event.key == pygame.K_d: playerX+=5
      #elif event.key == pygame.K_a: playerX+=-5
    if pygame.key.get_pressed()[pygame.K_w]==1: playerY+=-speed
    if pygame.key.get_pressed()[pygame.K_s]==1: playerY+=speed
    if pygame.key.get_pressed()[pygame.K_d]==1: playerX+=speed
    if pygame.key.get_pressed()[pygame.K_a]==1: playerX+=-speed
    if pygame.key.get_pressed()[pygame.K_SPACE]==1: 
      bullet = Bullet((playerX, playerY),0,30)
      bullet_list.add(bullet)
      bullet = Bullet((playerX, playerY),3,30)
      bullet_list.add(bullet)
      bullet = Bullet((playerX, playerY),-3,30)
      bullet_list.add(bullet)
    if debug:
      if pygame.key.get_pressed()[pygame.K_i]==1: speed+=-1
      if pygame.key.get_pressed()[pygame.K_o]==1: speed+=1
      if pygame.key.get_pressed()[pygame.K_p]==1: speed=default_speed
  #t1 = threading.Thread(target=lambda: input_game(playerX, playerY))
  #t1.daemon=True
  #t1.start()
  #starz.update()
  #starz.draw(screen)
  text = f"FPS: {round(clock.get_fps())}     Playtime: {round(playtime)}     speed={speed}"
  #pygame.display.set_caption(text)
  textsurface=myFont.render(text, False, (255,255,255))
  
  if playerX>screen.get_size()[0]: playerX=screen.get_size()[0]
  elif playerX<0: playerX=0
  if playerY<0: playerY=0
  elif playerY>screen.get_size()[1]: playerY=screen.get_size()[1]
  '''
  if ship<1:
    shipimage=ship1
    ship+=1
  elif ship<11 and ship>0:
    shipimage=ship3
    ship+=1
  elif ship<21 and ship>10:
    shipimage=ship3
    ship+=1
  elif ship<41 and ship>20:
    shipimage=ship1
    ship=0
  '''
  
  screen.blit(pygame.transform.scale(shipimage.get_next_frame(pygame.time.get_ticks()), (64,64)), (playerX-32, playerY-32))
  
  bullet_list.update()
  bullet_list.draw(screen)
  
  player = pygame.draw.circle(screen, (255, 28, 28), (round(playerX), round(playerY)), 3)
  
  if debug:
    screen.blit(textsurface,(0,0))
  else:
    pass
  pygame.display.flip()

pygame.quit()

print("-"*(16+len(str(round(playtime)))+9)+f"\nGame played for {round(playtime)} seconds.")


