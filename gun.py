import pygame
import time
import random

boxes = [pygame.image.load("gun_with_blocks/gun_box.png"), pygame.image.load("gun_with_blocks/ghost_box.png")]


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice(boxes)
        self.rect = self.image.get_rect().move(x, y)
        self.destination = 8

    def update(self, platforms):
        self.rect.y += self.destination
        if pygame.sprite.spritecollideany(self, platforms):
            self.destination = 0
            self.rect.y -= 1


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gun_with_blocks/gun.png")
        self.rect = self.image.get_rect().move(x, y)
        self.destination = 1
        self.next_box_time()

    def update(self, platforms):
        self.rect.x += self.destination
        if pygame.sprite.spritecollideany(self, platforms):
            self.destination *= -1

    def check_box(self):
        if time.time() > self.next_box:
            self.next_box_time()
            return Box(self.rect.x, self.rect.y)

    def next_box_time(self):
        self.next_box = time.time() + (1 + random.random()) * 5
