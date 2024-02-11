import pygame as pyg
import random
# Author: Wilson Neira
# Player class


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # create rect
        self.rect = pyg.Rect(self.x, self.y, 32, 32)
        # sprites
        self.up_sprites = []
        self.down_sprites = []
        # upload sprites
        up_sheet = pyg.image.load('reddragonfly4.png')
        # Split sheet into frames
        self.up_sprites = self.split_sheet(up_sheet)
        # upload sprites
        down_sheet = pyg.image.load('reddragonfly2.png')
        # Split sheet into frames
        self.down_sprites = self.split_sheet(down_sheet)
        # player movement
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        # player animation frames
        self.anim_frame = 0
        # player lives
        self.lives = 3

    def split_sheet(self, sheet):
        sprite_width = sheet.get_width() // 4
        sprite_height = sheet.get_height() // 4

        rows = sheet.get_height() // sprite_height
        cols = sheet.get_width() // sprite_width

        frames = []
        for i in range(rows):
            for j in range(cols):
                if i != 2 and j != 0:
                    frame = sheet.subsurface(j * sprite_width, i * sprite_height, sprite_width, sprite_height)
                    frames.append(frame)

        return frames

    def draw(self, w):
        # draw player
        self.rect.topleft = (self.x, self.y)
        pyg.draw.rect(w, "red", self.rect)

        if self.moving_up:
            w.blit(self.up_sprites[self.anim_frame], (self.x - 80, self.y - 80))
        elif self.moving_down:
            # Draw down animation
            w.blit(self.down_sprites[self.anim_frame], (self.x - 80, self.y - 80))
        self.anim_frame += 1
        if self.anim_frame >= len(self.up_sprites):
            self.anim_frame = 0

    # particles if player hits the enemy
    def explode(self, w):
        for i in range(20):
            x = self.x + random.randint(-10, 10)
            y = self.y + random.randint(-10, 10)
            pyg.draw.circle(w, 'red', (x, y), random.randint(2, 5))

    # particles if player collects a coin
    def collect(self, w):
        for i in range(20):
            x = self.x + random.randint(-5, 5)
            y = self.y + random.randint(-5, 5)
            pyg.draw.circle(w, 'yellow', (x, y), random.randint(2, 3))

    # particles if player runs into a wall
    def ouch(self, w):
        for i in range(5):
            x = self.x + random.randint(-10, 10)
            y = self.y + random.randint(-10, 10)
            pyg.draw.circle(w, 'white', (x, y), random.randint(2, 3))

    # particles if player loses
    def game_over(self, w):
        for i in range(100):
            x = random.randint(0, w.get_width())
            y = random.randint(0, w.get_height())
            pyg.draw.circle(w, 'red', (x, y), random.randint(4, 8))

    # particles if player wins
    def win(self, w):
        for i in range(200):
            x = random.randint(0, w.get_width())
            y = random.randint(0, w.get_height())
            color = random.choice(['yellow', 'green', 'blue'])
            pyg.draw.circle(w, color, (x, y), random.randint(2, 4))
