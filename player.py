#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os

MOVE_SPEED = 5
WIDTH = 22
HEIGHT = 33
COLOR = "#888888"
JUMP_POWER = 8.5
GRAVITY = 0.35  
ANIMATION_DELAY = 0.1 
ANIMATION_DELAY_2 = 0.1 
ICON_DIR = os.path.dirname(__file__) 
ICON_DIR_2 = os.path.dirname(__file__)

ANIMATION_RIGHT = [('%s/players/0.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/players/l1.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/players/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/players/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/players/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/players/0.png' % ICON_DIR, 0.1)]

ANIMATION_RIGHT_2 = [('%s/players/0_2.png' % ICON_DIR_2)]
ANIMATION_LEFT_2 = [('%s/players/r1.png' % ICON_DIR_2)]
ANIMATION_JUMP_LEFT_2 = [('%s/players/jl2.png' % ICON_DIR_2, 0.1)]
ANIMATION_JUMP_RIGHT_2 = [('%s/players/jr2.png' % ICON_DIR_2, 0.1)]
ANIMATION_JUMP_2 = [('%s/players/j2.png' % ICON_DIR_2, 0.1)]
ANIMATION_STAY_2 = [('%s/players/0_2.png' % ICON_DIR_2, 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  
        self.startX = x 
        self.startY = y
        self.yvel = 0  
        self.onGround = False  
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) 
        self.image.set_colorkey(Color(COLOR)) 

        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) 

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround: 
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0



class Player_2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.onGround = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))
        boltAnim = []
        for anim in ANIMATION_RIGHT_2:
            boltAnim.append((anim, ANIMATION_DELAY_2))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        boltAnim = []
        for anim in ANIMATION_LEFT_2:
            boltAnim.append((anim, ANIMATION_DELAY_2))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY_2)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT_2)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT_2)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP_2)
        self.boltAnimJump.play()

    def update(self, a, d, w, platforms):

        if w:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if a:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if w:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if d:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if w:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (a or d):
            self.xvel = 0
            if not w:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.d = p.rect.a

                if xvel < 0:
                    self.rect.a = p.rect.d

                if yvel > 0:
                    self.rect.s = p.rect.s
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.w = p.rect.w
                    self.yvel = 0
