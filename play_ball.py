# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:25:26 2020

@author: Cathig
"""
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from bear import Bear
from ball import Ball
from dog import Dog

class PlayBall:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set the window size and title bar text
        # Windowed
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Play Ball!")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.bear = Bear(self)
        self.balls = pygame.sprite.Group()
        self.dog = Dog(self)

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.bear.update()
                self._update_balls()
                self._update_dog()

            self._update_screen()

    def _update_dog(self):
        """Respond appropriately if the dog has reached an edge."""
        dog_direction = self.settings.dog_direction
        if self.dog.check_edges():
            dog_direction *= -1
        self.dog.update(dog_direction)

    def _update_balls(self):
        # Update ball positions.
        self.balls.update()

        # Get rid of balls that have disappeared.
        for ball in self.balls.copy():
            if ball.rect.left >= self.settings.screen_width:
                self.balls.remove(ball)
                self._ball_missed()

        self._check_ball_dog_collisions()

    def _check_ball_dog_collisions(self):
        """Respond to ball-dog collisions."""
        # When the ball reaches the dog, remove ball and dog and celebrate.
        if pygame.sprite.spritecollideany(self.dog, self.balls):
            self.balls.remove(ball)

        # Celebrate

    def _ball_missed(self):
        """Respond to ball misses."""
        if self.stats.balls_left > 0:
             #Decrement balls_left.
             self.stats.balls_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        # Gracefully exit when 'X' or alt+F4 close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit() - in text, but does not close gracefully
                # respond to other key presses
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """Start a new game."""
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of remaining balls.
        self.balls.empty()

        # Create a new dog and center the bear.
        self.dog.center_dog()
        self.bear.center_bear()

        # Hide the mouse pointer.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self,event):
        """Respond to key presses."""
        if event.key == pygame.K_DOWN:
            self.bear.moving_down = True
        elif event.key == pygame.K_UP:
            self.bear.moving_up = True
        elif event.key == pygame.K_q:
            pygame.quit()
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_SPACE:
            self._throw_ball()

    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.bear.moving_down = False
        elif event.key == pygame.K_UP:
            self.bear.moving_up = False

    def _throw_ball(self):
        """Create a new ball and toss it to the dog."""
        if len(self.balls) < self.settings.balls_allowed:
            new_ball = Ball(self)
            self.balls.add(new_ball)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.bear.blitme()
        self.dog.blitme()
        for ball in self.balls.sprites():
            ball.draw_ball()

        # Draw the Play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pb = PlayBall()
    pb.run_game()