from pygame import *
import pyganim
from bars import *

"""
обычная анимация для наших задач не очень подходит, поэтому испольуем pyganim, 
найденный на Хабре, с такими настройками:
"""
MOVE_SPEED = 5
WIDTH = 22
HEIGHT = 33
COLOR = "#888888"
JUMP_POWER = 8.5
GRAVITY = 0.35
ANIMATION_DELAY = 0.1
ANIMATION_DELAY_2 = 0.1

ANIMATION_RIGHT = [('players/0.png')]
ANIMATION_LEFT = [('players/l1.png')]
ANIMATION_JUMP_LEFT = [('players/jl.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('players/jr.png', 0.1)]
ANIMATION_JUMP = [('players/j.png', 0.1)]
ANIMATION_STAY = [('players/0.png', 0.1)]

ANIMATION_RIGHT_2 = [('players/0_2.png')]
ANIMATION_LEFT_2 = [('players/r1.png')]
ANIMATION_JUMP_LEFT_2 = [('players/jl2.png', 0.1)]
ANIMATION_JUMP_RIGHT_2 = [('players/jr2.png', 0.1)]
ANIMATION_JUMP_2 = [('players/j2.png', 0.1)]
ANIMATION_STAY_2 = [('players/0_2.png', 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y, red=False):
        self.box_num = 0
        if not red:
            self.color = "blue"
            self.anim_right = ANIMATION_RIGHT
            self.anim_left = ANIMATION_LEFT
            self.jump_left = ANIMATION_JUMP_LEFT
            self.jump_right = ANIMATION_JUMP_RIGHT
            self.jump_jump = ANIMATION_JUMP
            self.anim_stay = ANIMATION_STAY
        else:
            self.color = "red"
            self.anim_right = ANIMATION_LEFT_2
            self.anim_left = ANIMATION_RIGHT_2
            self.jump_left = ANIMATION_JUMP_LEFT_2
            self.jump_right = ANIMATION_JUMP_RIGHT_2
            self.jump_jump = ANIMATION_JUMP_2
            self.anim_stay = ANIMATION_STAY_2

        super().__init__()
        self.health_bar = Health(self.color)
        self.block_bar = Blocks(self.color)
        self.bar = sprite.Group(self.health_bar, self.block_bar)

        self.blocks_and_bullets = 10
        self.health = 10
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.onGround = False
        self.up, self.left, self.right = [False] * 3
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))
        boltAnim = []
        for anim in self.anim_right:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        boltAnim = []
        for anim in self.anim_left:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(self.anim_stay)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(self.jump_left)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(self.jump_right)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(self.jump_jump)
        self.boltAnimJump.play()

    def update(self, platforms):
        self.health_bar.update(self.health)
        self.block_bar.update(self.blocks_and_bullets)
        if self.rect.top > 700:
            self.kill()
            return
        if self.up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))
        if self.left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if self.up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
        if self.right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if self.up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))
        if not (self.left or self.right):
            self.xvel = 0
            if not self.up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        if self.health <= 0:
            self.kill()

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                elif xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
