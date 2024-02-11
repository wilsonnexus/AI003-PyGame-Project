import pygame as pyg

class Coin:
  def __init__(self, x, y):
    self.x = x 
    self.y = y
    # Collision
    self.rect = pyg.Rect(x, y, 20, 20) # coin rect
    # Collision

  def draw(self, w):
    # Collision
    self.rect.topleft = (self.x, self.y) # update rect 
    # Collision
    pyg.draw.circle(w, "yellow", (self.x, self.y), 10)
