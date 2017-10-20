import pygame

import data
import parallax

import coins
from config import *
from platforms import Platform, Trampoline


class Level(object):
    def __init__(self, player):
        self.level_elements = pygame.sprite.Group()

        self.player = player

        self.bg = parallax.ParallaxSurface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RLEACCEL)
        self.bg.add(data.filepath('backgrounds/sky.jpg'), 7)
        self.bg.add(data.filepath('backgrounds/back_buildings.png'), 5)
        self.bg.add(data.filepath('backgrounds/front_buildings.png'), 3)
        self.bg.add(data.filepath('backgrounds/ground.png'), 1)

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

    def update(self):
        self.level_elements.update()

    def draw(self, screen):
        self.bg.draw(screen)

        self.level_elements.draw(screen)

    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x
        self.bg.scroll(-shift_x, "horizontal")

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

        self.level_elements.add(coins.Coin((400, GROUND_HEIGHT - 100)))

