import pygame

import data

from config import *
import platforms


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = data.load_image("player.png")
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        self.level = None
        self.is_jumping = False

    def update(self):
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        print "HAHAHA", self.change_y
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.level_elements, False)
        for block in block_hit_list:
            if isinstance(block, platforms.Trampoline):
                print "jumpppp"
                self.jump()

            elif isinstance(block, platforms.Platform):

                # If we are moving right,
                # set our right side to the left side of the item we hit
                # if self.change_x > 0:
                #     self.rect.right = block.rect.left
                # elif self.change_x < 0:
                #     # Otherwise if we are moving left, do the opposite.
                #     self.rect.left = block.rect.right

                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                    self.change_y = 0
                    #     # elif self.change_y < 0:
                    #     #     self.rect.top = block.rect.bottom
                    #     pass


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 2

        if self.rect.y >= GROUND_HEIGHT - self.rect.height and self.change_y >= 0:

            self.change_y = 0
            # self.rect.y = GROUND_HEIGHT - self.rect.height

    def jump(self):
        self.change_y = -40

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0