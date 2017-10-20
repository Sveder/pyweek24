"""
Simple data loader module.

Loads data files from the "data" directory shipped with a game.

Enhancing this to handle caching etc. is left as an exercise for the reader.
"""

import os

import pygame


data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, "..", "data"))


def filepath(filename):
    return os.path.join(data_dir, filename)


def load(filename, mode="rb"):
    return open(os.path.join(data_dir, filename), mode)

def load_image(filename):
    return pygame.image.load(filepath(filename))
