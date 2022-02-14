import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute.
        self.image1 = pygame.image.load('images/alien.bmp')
        self.image2 = pygame.image.load('images/alien2.bmp')
        
        self.image = self.image1
        self.image_flag = 1

        self.rect = self.image1.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
      """Return True if alien is at edge of screen"""
      screen_rect = self.screen.get_rect()
      if self.rect.right >= screen_rect.right or self.rect.left <= 0:
        return True
        
    def update(self):
      """Move the alien to the right"""
      if(self.image_flag == 1):
        self.image = self.image2
        self.image_flag = 2
      else:
        self.image = self.image1
        self.image_flag = 1

      self.x += (self.settings.alien_speed * self.settings.fleet_direction)
      self.rect.x = self.x

