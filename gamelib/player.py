import pygame
from config import *

import data


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = data.load_image("player.png")
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move left/right
        self.rect.x += self.change_x

        self.rect.y -= self.change_y
        self.change_y = max(0, self.change_y - 1)

    def jump(self):
        self.change_y = 20

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0