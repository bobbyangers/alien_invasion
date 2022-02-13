import json
class GameStats:
  """Track statistics for Alien Invasion."""

  def __init__(self, ai_game):
    """Initialize statitics."""
    self.settings = ai_game.settings
    self.reset_stats()

    # Start Alien Invasion in an active state.
    self.game_active = False

    # High score should never be reset.
    self.high_score = 0    

    self.level = 0
    self.score = 0

  def reset_stats(self):
    """Initialize statistics that ca change during the game."""      
    self.ships_left = self.settings.ship_limit
    self.score = 0
    self.level = 1

    with open('game_stats.json') as f:
      data = json.load(f)

    self.high_score = int(data['all_time_high_score'])

  def save_high_score(self):    
    data = {
      'all_time_high_score' : self.high_score
    }

    with open('game_stats.json', 'w') as f:
       json.dumps(data, f, indent = 4, sort_keys=True)
