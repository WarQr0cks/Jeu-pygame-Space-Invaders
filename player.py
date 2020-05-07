import pygame as pg
from fire import Fire
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 100
        self.max_hp = 100
        self.damage = 10
        self.speed = 6
        self.all_fire = pg.sprite.Group()
        self.image = pg.image.load('assets/player.png')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 700
    def degats(self, amount):
        if self.hp - amount > amount:
            self.hp -= amount
    def update_hp_bar(self,surface):
        pg.draw.rect(surface, (107, 102, 111), [self.rect.x, self.rect.y+120, self.max_hp, 5])
        pg.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y+120, self.hp, 5])
    def fire(self):
        self.all_fire.add(Fire(self))
    def right(self):
            self.rect.x += self.speed
    def left(self):
            self.rect.x -= self.speed