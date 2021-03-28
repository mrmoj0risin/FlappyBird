import pygame
# import neat
# import time
import os
# import sys
from Pipe import Pipe
from Bird import Bird
from Base import Base
pygame.font.init()
pygame.font.SysFont('arial', 36)

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))

    f1 = pygame.font.Font(None, 36)
    score_draw = f1.render('Score ' + str(score), True, (100, 100, 0))

    for pipe in pipes:
        pipe.draw(win)

    win.blit(score_draw, (10, 10))
    base.draw(win)

    bird.draw(win)
    pygame.display.update()


def game_over(win, base, score):
    win.blit(BG_IMG, (0, 0))
    base.draw(win)
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Hello Привет', True,
                      (100, 100, 0))

    f2 = pygame.font.SysFont('serif', 48)
    text2 = f2.render("Final Score is " + str(score), False, (0, 180, 0))
    win.blit(text1, (100, 300))
    win.blit(text2, (100, 400))
    pygame.display.update()


def main():
    score = 0
    bird = Bird(200, 320)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    game = True

    while run:
        clock.tick(25)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB or pygame.K_SPACE:

                    bird.jump()

            if event.type == pygame.QUIT:
                run = False

        if game:
            rem = []

            add_pipe = False
            for pipe in pipes:
                if pipe.collide(bird, win):
                    game = False
                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True
                pipe.move()
            if add_pipe:
                score += 1

                pipes.append(Pipe(700))

            for r in rem:
                pipes.remove(r)
                pipe.move()

        if bird.y + bird.img.get_height() >= 700:
            game = False

        base.move()
        if game:
            bird.move()

            draw_window(win, bird, pipes, base, score)
        else:
            game_over(win, base, score)

    pygame.quit()
    quit()


main()
