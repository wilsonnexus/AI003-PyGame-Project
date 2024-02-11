import pygame as pyg

class Grid():
    def __init__(self, width, height, cols, rows):
        self.width = width
        self.height = height
        self.cols = cols
        self.rows = rows
        self.cell_width = width // cols
        self.cell_height = height // rows
	# Coin.py
        self.objects = []
	# Coin.py
    
    def draw(self, w):
        for i in range(self.cols):
            for j in range(self.rows):
                rect = pyg.Rect(i * self.cell_width, j * self.cell_height,
                                self.cell_width, self.cell_height)
                pyg.draw.rect(w, "white", rect, 1)
	# Coin.py
        for obj in self.objects:
            obj.draw(w)
	# Coin.py
