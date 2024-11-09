import pygame as pg
import math

rocket_image = pg.image.load('Images/Ракета.png')

class Rocket(pg.sprite.Sprite):
    def __init__(self, center, corner):
        pg.sprite.Sprite.__init__(self)
        self.corner = corner
        self.speed = 17
        self.image = pg.transform.scale(rocket_image, [32, 32])
        new_image = pg.transform.rotate(self.image, self.corner)
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.start = center
        self.radius = 10
        self.last_update = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 25:  # если прошло достаточно времени
            self.last_update = now
            self.rect.x += self.speed * math.cos(math.radians(90 + self.corner))
            self.rect.y += -self.speed * math.sin(math.radians(90 + self.corner))

            # Проверка на дальность полета
            if math.sqrt((self.rect.center[0] - self.start[0])**2 + (self.rect.center[1] - self.start[1])**2) > 450:
                self.kill()
