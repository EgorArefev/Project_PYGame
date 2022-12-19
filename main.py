import pygame
from player import *
from blocks import *


WIN_WIDTH = 988
WIN_HEIGHT = 598 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_IMAGE = pygame.image.load('background-color/background_color_1.jpg')


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l) 
    l = max(-(camera.width - WIN_WIDTH), l) 
    t = max(-(camera.height - WIN_HEIGHT), t) 
    t = min(0, t)

    return Rect(l, t, w, h)


def make_level():
    global level, platforms, entities, hero, hero_2
    entities = pygame.sprite.Group()
    entities.add(hero)
    entities.add(hero_2)
    platforms = []
    x = y = 0 
    for row in level: 
        for col in row: 
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0 


def main():
    global level, entities, platforms, hero, hero_2
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("Super Mario Boy") 
    clock = pygame.time.Clock()
    bg = Surface((WIN_WIDTH, WIN_HEIGHT)) 

    hero_2 = Player(55, 514)
    left = right = False
    up = False

    hero = Player(835, 514) 
    a = d = False 
    w = False

    entities = pygame.sprite.Group()
    platforms = [] 

    entities.add(hero)
    entities.add(hero_2)

    level = [
        "-                                    -",
        "-                                    -",
        "-                                    -",
        "-                                    -",
        "-----                            -----",
        "---     *                    *     ---",
        "--    ---                    ---    --",
        "-      --                    --      -",
        "-       -                    -       -",
        "-       ---                ---       -",
        "--   -----                  -----   --",
        "-       -                    -       -",
        "-       *                    *       -",
        "-      --                    --      -",
        "---     -                    -     ---",
        "--      *                    *      --",
        "-     ----                  ----     -",
        "-        -                  -        -",
        "-----    *                  *    -----",
        "-       --                  --       -",
        "-                                    -",
        "-                                    -",
        "--------------------------------------",
        "--------------------------------------"]

    make_level()

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)
    running = True

    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN:
                if e.key == K_w:
                    w = True
                elif e.key == K_a:
                    a = True
                elif e.key == K_d:
                    d = True
                elif e.key == K_s:
                    new_l = list(map(list, level))
                    if new_l[hero_2.rect.y // 26 + 2][hero_2.rect.x // 26] == " ":
                        new_l[hero_2.rect.y // 26 + 2][hero_2.rect.x // 26] = "-"
                        level = list(map("".join, new_l))
                        make_level()
                elif e.key == K_UP:
                    up = True
                elif e.key == K_LEFT:
                    left = True
                elif e.key == K_RIGHT:
                    right = True
                elif e.key == K_DOWN:
                    new_l = list(map(list, level))
                    if new_l[hero.rect.y // 26 + 2][hero.rect.x // 26] == " ":
                        new_l[hero.rect.y // 26 + 2][hero.rect.x // 26] = "-"
                        level = list(map("".join, new_l))
                        make_level()

            elif e.type == KEYUP:
                if e.key == K_w:
                    w = False
                elif e.key == K_d:
                    d = False
                elif e.key == K_a:
                    a = False
                elif e.key == K_UP:
                    up = False
                elif e.key == K_RIGHT:
                    right = False
                elif e.key == K_LEFT:
                    left = False

        screen.blit(BACKGROUND_IMAGE, (0, 0))
        hero.update(left, right, up, platforms)
        hero_2.update(a, d, w, platforms)
        entities.draw(screen)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()
        clock.tick(75)


if __name__ == "__main__":
    main()
