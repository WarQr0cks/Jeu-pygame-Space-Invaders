import pygame as pg
from random import *
def random_image():
    a = randint(1, 2)
    if a == 1:
        b = 'assets/alien 1.png'
    else:
        b = 'assets/alien 2.png'
    return b
class Alien(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 20
        self.max_hp = 20
        self.damage = 10
        self.image = pg.image.load(random_image())
        self.image = pg.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 820)
        self.rect.y = randint(-400, -100)
        self.speed = randint(3, 5)
    def degats(self, amount):
        self.hp -= amount

    def update_hp_bar(self,surface):
        pg.draw.rect(surface, (107, 102, 111), [self.rect.x, self.rect.y - 10, self.max_hp * 4, 5])
        pg.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y-10, self.hp*4, 5])
        if self.hp <= 0 or self.rect.y >= 950:
            self.hp = self.max_hp
            self.rect.y = randint(-400, -100)
            self.rect.x = randint(0, 820)
            self.speed = randint(3, 5)
    def down(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.speed
            if self.rect.y >= 950:
                self.game.player.degats(self.damage)
        else:
            self.game.player.degats(self.damage)
            self.hp = 0