import pygame as pg

explosion_image = pg.image.load('Images/Взрыв.png')
class Explosion(pg.sprite.Sprite):
    def __init__(self, size, center):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(explosion_image, [size, size])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 1500:  # если прошло достаточно времени
            self.kill()