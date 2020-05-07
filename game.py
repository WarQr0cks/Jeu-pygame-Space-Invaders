import pygame as pg
from player import Player
from aliens import *
class Game:
    def __init__(self):
        self.all_players = pg.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_aliens = pg.sprite.Group()
        self.pressed = {}
        self.summon_alien()
        self.summon_alien()
        self.summon_alien()
    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)
    def summon_alien(self):
        alien = Alien(self)
        self.all_aliens.add(alien)
