import pygame as pyg
# Author: Wilson Neira
# Enemy class


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # create rect
        self.rect = pyg.Rect(self.x, self.y, 32, 32)

    def draw(self, w):
        # Draw enemy
        self.rect.topleft = (self.x, self.y)
        pyg.draw.rect(w, "blue", self.rect)