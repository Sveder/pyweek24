import pygame

import data

from config import *
from platforms import Platform, Trampoline


class Level(object):
    def __init__(self, player, bg="bg.jpg"):
        self.level_elements = pygame.sprite.Group()

        self.player = player

        self.bg = data.load_image(bg)
        bg_width = max(self.bg.get_rect().width, SCREEN_WIDTH)
        bg_height = max(self.bg.get_rect().height, SCREEN_HEIGHT)
        self.bg = pygame.transform.scale(self.bg, (bg_width, bg_height))

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

    def update(self):
        self.level_elements.update()

    def draw(self, screen):
        screen.blit(self.bg, (self.world_shift, 0))
        self.level_elements.draw(screen)

    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.level_elements:
            platform.rect.x += shift_x


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.level_limit = -1500

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.level_elements.add(block)

        trampoline = Trampoline()
        trampoline.rect.x = 400
        trampoline.rect.y = GROUND_HEIGHT - 3
        self.level_elements.add(trampoline)

