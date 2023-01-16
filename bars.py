import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(0, 0, 180, 30)
        self.rect.x = 788 if color == "blue" else 20


class Health(Bar):
    def __init__(self, color):
        super().__init__(color)
        self.rect.y = 550
