import pygame
import time
import random

WIN_WIDTH = 988

boxes = [pygame.image.load("gun_with_blocks/gun_box.png"),
         pygame.image.load("gun_with_blocks/ghost_box.png")]


def opponent_color(color):
    return "red" if color == "blue" else "blue"


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = boxes[0]
        self.type = drops[0]
        self.rect = self.image.get_rect().move(x, y)
        self.destination = 8

    def make_drop(self, color):
        self.kill()
        return self.type(color)

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
        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.destination *= -1

    def check_box(self):
        if time.time() > self.next_box:
            self.next_box_time()
            return Box(self.rect.x, self.rect.y)

    def next_box_time(self):
        self.next_box = time.time() + (1 + random.random()) * 5


class Ghost(pygame.sprite.Sprite):
    image = pygame.image.load("gun_with_blocks/ghost.png")

    def __init__(self, color):
        super().__init__()
        self.color = opponent_color(color)
        self.rect = self.image.get_rect().move(500, -100)

    def update(self, heroes):
        hero = tuple(filter(lambda x: x.color == self.color, heroes.sprites()))[0]
        x, y = hero.rect.x, hero.rect.y
        x_s, y_s = self.rect.x, self.rect.y
        s = ((x_s - x) ** 2 + (y_s - y) ** 2) ** 0.5 // 1
        x_to = (x - x_s) / (s / 2) // 1
        y_to = (y - y_s) / (s / 2) // 1
        self.rect = self.rect.move(x_to, y_to)
        if hero := pygame.sprite.spritecollideany(self, heroes):
            hero.health -= 2
            self.kill()
            #.move(300, random.randint(100, 500))


class Tourell(pygame.sprite.Sprite):
    #image = pygame.image.load("gun_with_blocks/tourel.png")

    def __init__(self, color):
        super().__init__()
        self.rect = self.image.get_rect().move(x, y)


drops = [Ghost, Tourell]
