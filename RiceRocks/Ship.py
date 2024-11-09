import pygame as pg
import math

ship_image = pg.image.load('Images/Корабль.png')
ship_with_fire_image = pg.image.load('Images/Корабль с огнем.png')

class Ship(pg.sprite.Sprite):
    def __init__(self, x, y, field_size):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = pg.transform.scale(ship_image, [60, 60])
        self.image_orig_fly = pg.transform.scale(ship_with_fire_image, [50, 50])
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.WIDTH = field_size[0]
        self.HEIGHT = field_size[1]
        self.rect.center = (self.WIDTH / 2, self.HEIGHT / 2)
        self.radius = 20
        self.corner = 0
        self.speed = 0
        self.last_update = pg.time.get_ticks()

    def update(self):
        self.speed = 0
        self.speed_fly = 0

        keystate = pg.key.get_pressed()  # проверка нажатия клавиш
        if keystate[pg.K_LEFT]:
            self.speed = 9
        if keystate[pg.K_RIGHT]:
            self.speed = -9
        if keystate[pg.K_UP]:
            self.speed_fly = 9

        now = pg.time.get_ticks()
        if now - self.last_update > 25:  # если прошло достаточно времени
            self.last_update = now
            self.corner = (self.corner + self.speed) % 360
            if self.speed_fly == 0:
                new_image = pg.transform.rotate(self.image_orig, self.corner)
            else:
                new_image = pg.transform.rotate(self.image_orig_fly, self.corner)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

            self.rect.x += self.speed_fly * math.cos(math.radians(90 + self.corner))
            self.rect.y += -self.speed_fly * math.sin(math.radians(90 + self.corner))

            if self.rect.x < 0 or self.rect.x > self.WIDTH:
                self.rect.x = abs(self.rect.x - self.WIDTH)
            if self.rect.y < 0 or self.rect.y > self.HEIGHT:
                self.rect.y = abs(self.rect.y - self.HEIGHT)


