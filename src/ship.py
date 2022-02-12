import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.center_ship()

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
      """Update the ship's position based on the movement flag."""
      if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.settings.ship_speed
      elif self.moving_left and self.rect.left > 0:
        self.x -= self.settings.ship_speed

      self.rect.x = self.x

    def blitme(self):
      """Draw the ship at its current location."""
      self.screen.blit(self.image, self.rect)

    def center_ship(self):
      """Center the ship on the screen."""
      self.rect.midbottom = self.screen_rect.midbottom
        
      #Store a decimal value fo the ship's horizontal position.
      self.x = float(self.rect.x)
