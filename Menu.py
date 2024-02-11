import pygame as pyg
import sys
from Button import Button
from Grid import Grid
from Player import Player
from Coin import Coin
from Enemy import Enemy
import random


class Menu:
    def __init__(self):
        pyg.init()
        self.w = pyg.display.set_mode((640, 480))

        # width and height of game window
        self.width, self.height = self.w.get_size()

        # rectangle from our game window
        self.wr = self.w.get_rect()
        # title font
        self.title_font = pyg.font.SysFont("Concord", 75, True, False)

        # button font
        font = pyg.font.SysFont(pyg.font.get_fonts()[0], 25, True, False)

        self.startButton = Button(font, "Start", fc = "white", bg  = "lightgreen", border = "white",
                                  pos=(self.width // 2 - 100, 240), width=200, pad=(75, 10))

        # grid
        self.grid = None
        # player
        self.player = None
        # enemy
        self.enemy = None
        # collected coins
        self.total_coins = 6
        self.coins_text = 0
        # grid cols
        self.cols = 10
        # grid rows
        self.rows = 10

    def gameloop(self):
        while True:
            self.w.fill("lightblue")
            # event loop
            for e in pyg.event.get():
                if e.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
            if self.grid:
                self.grid.draw(self.w)
            else:
                # draw title
                title = self.title_font.render("AI003", True, "black")
                self.w.blit(title, title.get_rect(midtop = self.wr.midtop))
                # draw the button and give an indication that the button was pressed
                if self.startButton.draw(self.w):
                    # Create Grid
                    self.grid = Grid(self.width, self.height, self.cols, self.rows)
                    # Create Enemy
                    self.enemy = Enemy(300, 300)
                    # Create Player
                    self.player = Player(50, 50)
                    # Create Coins
                    self.generate_coins()

            # Record Key
            key = pyg.key.get_pressed()
            dist = 5

            # player animation movement
            if self.player:
                if key[pyg.K_UP]:
                    self.player.moving_up = True
                elif key[pyg.K_DOWN]:
                    self.player.moving_down = True
                elif key[pyg.K_LEFT]:
                    self.player.moving_left = True
                elif key[pyg.K_RIGHT]:
                    self.player.moving_right = True
                else:
                    self.player.moving_up = False
                    self.player.moving_down = False
                    self.player.moving_left = False
                    self.player.moving_right = False
            # Movement
            if self.player and key[pyg.K_UP] and self.player.y - dist > 0:
                self.player.y -= dist

            if self.player and key[pyg.K_DOWN] and self.player.y + dist < self.height - 32:
                self.player.y += dist

            if self.player and key[pyg.K_LEFT] and self.player.x - dist > 0:
                self.player.x -= dist

            if self.player and key[pyg.K_RIGHT] and self.player.x + dist < self.width - 32:
                self.player.x += dist

            # wall particles
            if self.player and (self.player.x <= 5 or self.player.x >= self.width - 40):
                self.player.ouch(self.w)

            if self.player and (self.player.y <= 5 or self.player.y >= self.height - 40):
                self.player.ouch(self.w)

            # Enemy Movement
            dist_enemy = 3
            if self.enemy:
                if self.enemy.x < self.player.x:
                    self.enemy.x += dist_enemy
                if self.enemy.x > self.player.x:
                    self.enemy.x -= dist_enemy
                if self.enemy.y < self.player.y:
                    self.enemy.y += dist_enemy
                if self.enemy.y > self.player.y:
                    self.enemy.y -= dist_enemy


            # Remove objects from self.grid.objects
            if self.grid:
                for obj in self.grid.objects:
                    if self.player.rect.colliderect(obj.rect):
                        self.player.collect(self.w)
                        # object collected, remove it
                        self.grid.objects.remove(obj)
                        # collected
                        self.total_coins -= 1
                        self.coins_text += 1

            if self.player:
                # display the character lives text
                lives_font = pyg.font.SysFont("Arial", 24)
                lives_text = lives_font.render("Lives: " + str(self.player.lives), True, "Red")
                self.w.blit(lives_text, (10, 10))

                # display coins text
                coins_font = pyg.font.SysFont("Arial", 24)
                coins_render = coins_font.render("Coins: " + str(self.coins_text), True, "Yellow")
                self.w.blit(coins_render, (100, 10))
                self.enemy.draw(self.w)
                self.player.draw(self.w)

                # if player touches the enemy
                if self.player.rect.colliderect(self.enemy.rect) and self.player.lives > 0:
                    # explosion particle effects
                    self.player.explode(self.w)
                    # reduce player lives by 1
                    self.player.lives -= 1
                    # update character lives text
                    pyg.display.update()
                    # reset character positions
                    self.player.x = 50
                    self.player.y = 50
                    self.enemy.x = 300
                    self.enemy.y = 300
                    # once the player hits 0 lives
                    if self.player.lives == 0:
                        # losing particles
                        self.player.game_over(self.w)
                        # game over text
                        game_over_font = pyg.font.SysFont("Arial", 72)
                        game_over_text = game_over_font.render("Game Over", True, "Red")
                        self.w.blit(game_over_text, (self.width / 2 - 150, self.height / 2 - 50))
                        pyg.display.update()
                        # pause for 1.5 seconds
                        pyg.time.delay(1500)
                        # restart game
                        menu = Menu()
                        menu = menu.gameloop()

            if self.total_coins == 0:
                # particles if game won
                self.player.win(self.w)
                # win game text
                game_win_font = pyg.font.SysFont("Arial", 72)
                game_win_text = game_win_font.render("You Win!", True, "Green")
                self.w.blit(game_win_text, (self.width / 2 - 150, self.height / 2 - 50))
                pyg.display.update()
                # pause for 1.5 seconds
                pyg.time.delay(1500)
                # restart game
                menu = Menu()
                menu = menu.gameloop()

            pyg.display.update()
            pyg.event.pump()
            pyg.time.delay(30)

    # generate random coins
    def generate_coins(self):
        while len(self.grid.objects) < self.total_coins:
            x = random.randint(0, self.width - 32)
            y = random.randint(0, self.height - 32)

            # Check if coin overlaps with player or enemy
            if (x, y) != (self.player.x, self.player.y) and (x, y) != (self.enemy.x, self.enemy.y):
                coin = Coin(x, y)
                self.grid.objects.append(coin)


# program execution starts here
menu = Menu()
menu = menu.gameloop()
