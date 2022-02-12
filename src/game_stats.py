class GameStats:
  """Track statistics for Alien Invasion."""

  def __init__(self, ai_game):
    """Initialize statitics."""
    self.settings = ai_game.settings
    self.reset_stats()

  def reset_stats(self):
      """Initialize statistics that ca change during the game."""
      self.ships_left = self.settings.ship_limit