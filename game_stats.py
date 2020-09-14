# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:20:30 2020

@author: Cathig
"""
class GameStats:
    """Track statistics for Play Ball."""

    def __init__(self, pb_game):
        """Initialize statistics."""
        self.settings = pb_game.settings
        self.reset_stats()
        # Start Play Ball in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.balls_left = self.settings.ball_limit