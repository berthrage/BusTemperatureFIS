import pygame

class Rect:
    def __init__(self, left, top, width, height):
        self.rect = pygame.rect.Rect(left, top, width, height)