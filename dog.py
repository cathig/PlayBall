# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:08:35 2020

@author: Cathig
"""
import pygame

class Dog:
    def __init__(self, pb_game):
        """Initialize the dog and set its starting position."""
        self.screen = pb_game.screen
        self.settings = pb_game.settings
        self.screen_rect = pb_game.screen.get_rect()

        # Load the dog image and get its rect.
        self.image = pygame.image.load('images/dog.png')
        self.rect = self.image.get_rect()

        # Start the dog at the center right of the screen.
        self.rect.midright = self.screen_rect.midright

        # Store a decimal value for the dog's vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if the dog is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self, dog_direction):
        """Move the dog down or up."""
        self.y += (self.settings.dog_speed * dog_direction)
        self.rect.y = self.y

    def center_dog(self):
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the dog at its current location."""
        self.screen.blit(self.image, self.rect)