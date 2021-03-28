import pygame
import os
import random

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

class Pipe:
    GAP = 185
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.gap = 100
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG
        self.height = 50

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.bottom = self.height + self.GAP
        self.top = self.height - self.PIPE_TOP.get_height()

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird, win):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_ofset = (self.x - bird.x, self.top - round(bird.y))
        bottom_ofset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_ofset)
        t_point = bird_mask.overlap(top_mask, top_ofset)
        if t_point or b_point:
            return True
        return False

