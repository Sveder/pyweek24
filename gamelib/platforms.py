import pygame
from pygame.colordict import THECOLORS

import data


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(THECOLORS["green"])

        self.rect = self.image.get_rect()


class Trampoline(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = data.load_image("trampoline.png")
        self.rect = self.image.get_rect()
