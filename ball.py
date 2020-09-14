# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:48:06 2020

@author: Cathig
"""
import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class to manage balls tossed by the bear."""

    def __init__(self, pb_game):
        """Create a ball object at the bear's current position."""
        super().__init__()
        self.screen = pb_game.screen
        self.settings = pb_game.settings
        self.screen_rect = pb_game.screen.get_rect()

        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.midright = pb_game.bear.rect.center

        # Store the ball's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the ball across the screen."""
        # Update the decimal position of the ball.
        self.x += self.settings.ball_speed
        # Update the rect position
        self.rect.x = self.x

    def blitme(self):
        """Draw the ball to the screen."""
        self.screen.blit(self.image, self.rect)