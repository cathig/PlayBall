# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:16:31 2020

@author: Cathig
"""
class Settings:
    """A class to store all settings for Play Catch."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 230, 80)

        # Ball settings
        self.ball_speed = 1.0
        self.ball_limit = 3
        self.balls_allowed = 3

        # Dog settings
        self.dog_speed = 1.0
        # dog direction of 1 represents down; -1 represents up.
        self.dog_direction = 1

        # Bear settings
        self.bear_speed = 1.5