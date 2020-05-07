import pygame as pg

class Fire(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.speed = 8
        self.player = player
        self.image = pg.image.load('assets/projectile.png')
        self.image = pg.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+38
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0
    def rotate(self):
        self.angle += 12
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_fire.remove(self)
    def move(self):
        self.rect.y -= self.speed
        self.rotate()
        for alien in self.player.game.check_collision(self, self.player.game.all_aliens):
            self.remove()
            alien.degats(self.player.damage)
        if self.rect.y < -50:
            self.remove()
