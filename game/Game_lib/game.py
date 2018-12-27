import pygame

UP=1
DOWN=2
LEFT=3
RIGHT=4

class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((10, 20))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
    self.speedy = -10
  def update(self):
    self.rect.y += self.speedy
    # kill if it moves off the top of the screen
    if self.rect.bottom < 0:
      self.kill()

class Game:
  def __init__(self, screen, display):
    print("Using Game-lib v1.0")
    self.sc=screen
    self.dis=display
    
  def shoot(self, start_pos, speed, direction=UP):
    pass
def game(screen, display): return Game(screen, display)

if __name__ == '__name__':
  pass
