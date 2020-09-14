# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:57:14 2020

@author: Cathig
"""
import pygame

class Bear:
    """A class to manage the bear's vertical movement and ball tosses."""

    def __init__(self, pb_game):
        """Initialize the bear and set its starting position."""
        self.screen = pb_game.screen
        self.settings = pb_game.settings
        self.screen_rect = pb_game.screen.get_rect()

        # Load the bear image and get its rect.
        self.image = pygame.image.load('images/bear.png')
        self.rect = self.image.get_rect()

        # Start the bear at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the bear's vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the bear's position based on the movement flag."""
        # Update the bear's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bear_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.bear_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def center_bear(self):
        """Center the bear on the left side of the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the bear at its current location."""
        self.screen.blit(self.image, self.rect)