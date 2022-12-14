import pygame
from pygame import *

WIN_WIDTH = 988
WIN_HEIGHT = 598
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#ffd299"
PLATFORM_WIDTH = 26
PLATFORM_HEIGHT = 26
PLATFORM_COLOR = "#FF6262"
PLATFORM_COLOR_2 = "#FF6454"


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario Boy")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

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

    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            if col == "*":
                pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR_2))
                screen.blit(pf, (x, y))

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
        screen.blit(bg, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
