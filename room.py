import pygame
from settings import *


class Room(pygame.sprite.Sprite):
    def __init__(self, pos, groups, roomtype):
        super().__init__(groups)
        self.pos = pos
        self.roomtype = roomtype
        self.rect = pygame.Rect(pos, (ROOMSIZE, ROOMSIZE))