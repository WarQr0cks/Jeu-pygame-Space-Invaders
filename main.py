import pygame as pg
from game import Game
pg.init()

pg.display.set_caption("SpaceShooter")

screen = pg.display.set_mode((900, 900))
bg = pg.image.load('assets/bg.jpg')
game = Game()

run = True

while run:
    screen.blit(bg,(0,0))
    screen.blit(game.player.image, game.player.rect)
    game.player.update_hp_bar(screen)
    for fire in game.player.all_fire:
        fire.move()
    for alien in game.all_aliens:
        alien.down()
        alien.update_hp_bar(screen)
    game.player.all_fire.draw(screen)
    game.all_aliens.draw(screen)
    if game.pressed.get(pg.K_RIGHT) and game.player.rect.x + game.player.rect.width - 175 < 720:
        game.player.right()
    elif game.pressed.get(pg.K_LEFT) and game.player.rect.x > 0:
        game.player.left()
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pg.K_SPACE:
                game.player.fire()
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False