import sys

import pygame.sprite

from player import *
from blocks import *
from gun import *

WIN_WIDTH = 988
WIN_HEIGHT = 598
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_IMAGE = pygame.image.load('background-color/background_color_1.jpg')


def make_level():
    global level, platforms, entities, hero, hero_2, gun
    entities = pygame.sprite.Group()
    entities.add(hero)
    entities.add(hero_2)
    entities.add(gun)
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


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


def start_screen():
    intro_text = ["Чтобы выбрать уровень введите", "число на клавиатуре от 1 до 2"]

    fon = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 36)
    text_coord = 250
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 300
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    hero = pygame.transform.scale(pygame.image.load("players/0.png"), (110, 165))
    screen.blit(hero, (325, 50))
    hero = pygame.transform.scale(pygame.image.load("players/0_2.png"), (110, 165))
    screen.blit(hero, (525, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(60)


def main():
    global level, entities, platforms, hero, hero_2, gun

    hero_2 = Player(55, 514)
    hero = Player(835, 514, red=1)
    heroes = pygame.sprite.Group()
    heroes.add(hero, hero_2)

    gun = Gun(400, 5)

    all_boxes = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    all_drops = pygame.sprite.Group()
    platforms = []

    entities.add(hero)
    entities.add(hero_2)
    entities.add(gun)

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

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN:
                if e.key == K_w:
                    hero_2.up = True
                    #w = True
                elif e.key == K_a:
                    hero_2.left = True
                    #a = True
                elif e.key == K_d:
                    hero_2.right = True
                    #d = True
                elif e.key == K_s:
                    new_l = list(map(list, level))
                    print(0)
                    if new_l[hero_2.rect.y // 26 + 2][hero_2.rect.x // 26] == " ":
                        new_l[hero_2.rect.y // 26 + 2][hero_2.rect.x // 26] = "-"
                        level = list(map("".join, new_l))
                        make_level()
                elif e.key == K_UP:
                    hero.up = True
                elif e.key == K_LEFT:
                    hero.left = True
                elif e.key == K_RIGHT:
                    hero.right = True
                elif e.key == K_DOWN:
                    new_l = list(map(list, level))
                    if new_l[hero.rect.y // 26 + 2][hero.rect.x // 26] == " ":
                        new_l[hero.rect.y // 26 + 2][hero.rect.x // 26] = "-"
                        level = list(map("".join, new_l))
                        make_level()

            elif e.type == KEYUP:
                if e.key == K_w:
                    hero_2.up = False
                elif e.key == K_d:
                    hero_2.right = False
                elif e.key == K_a:
                    hero_2.left = False
                elif e.key == K_UP:
                    hero.up = False
                elif e.key == K_RIGHT:
                    hero.right = False
                elif e.key == K_LEFT:
                    hero.left = False

        if col := pygame.sprite.spritecollideany(hero, all_boxes):
            all_drops.add(col.make_drop(hero.color))

        if col := pygame.sprite.spritecollideany(hero_2, all_boxes):
            all_drops.add(col.make_drop(hero_2.color))
        #if hero. тут надо сделать проверку жив ли чел или сделать завершение игры со смертью - сделал

        screen.blit(BACKGROUND_IMAGE, (0, 0))
        gun.update(platforms)
        box = gun.check_box()
        if box:
            all_boxes.add(box)
        hero.update(platforms)
        hero_2.update(platforms)
        all_boxes.draw(screen)
        all_boxes.update(platforms)

        all_drops.draw(screen)
        try:
            all_drops.update(heroes)
        except:
            print(f"Выиграл {heroes.sprites()[0].color}")
        entities.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Гора: Анычар")
    clock = pygame.time.Clock()

    start_screen()
    main()