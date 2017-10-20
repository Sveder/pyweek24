import pygame

from config import *
import data


class Shmuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = data.load_image("shmuel.png")

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 20 - self.rect.width
        self.rect.y = 20


