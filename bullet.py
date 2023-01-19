import pygame
from math import atan, degrees


class Bullet(pygame.sprite.Sprite):
    image = pygame.image.load("gun_with_blocks/bullet.png")

    def __init__(self, x, y, x_s, y_s):
        print(9)
        super().__init__()
        print(633)
        s = ((x_s - x) ** 2 + (y_s - y) ** 2) ** 0.5 // 1
        self.x_to = -(x - x_s) / (s / 10) // 1
        self.y_to = -(y - y_s) / (s / 10) // 1
        print(y_s, y, x_s, x)
        try:
            angle = (y_s - y) / (x_s - x)
        except ZeroDivisionError:
            angle = 0
        angle = degrees(atan(angle))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect().move(x, y)

    def update(self, heroes, boxes):
        self.rect = self.rect.move(self.x_to, self.y_to)
        if self.rect.top < 0 or self.rect.top > 800:
            self.kill()
        if box := pygame.sprite.spritecollideany(self, boxes):
            box.health -= 1
            self.kill()
        print(self.rect.top)