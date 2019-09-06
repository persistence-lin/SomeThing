#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
""" 
@author:linzhongjie
@file: CodeRain.py 
@time: 2019/09/06 
"""
import random
import pygame


class CodeRain(object):

    panel_width = 1080
    panel_height = 800
    font_p = 15

    def play_code(self):

        pygame.init()
        win = pygame.display.set_mode((self.panel_width, self.panel_height), 32)
        font = pygame.font.SysFont("SourceCodePro-Black.ttf", 25)
        bg = pygame.Surface((self.panel_width, self.panel_height), flags=pygame.SRCALPHA)
        pygame.Surface.convert(bg)
        bg.fill(pygame.Color(0, 0, 0, 25))
        win.fill((0, 0, 0))

        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        texts = [font.render(str(letter[i]), True, (0, 255, 0)) for i in range(20)]

        column = int(self.panel_width / self.font_p)
        drops = [i for i in range(column)]

        while True:

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    change = pygame.key.get_pressed()
                    if change[32]:
                        exit()
            pygame.time.delay(60)

            win.blit(bg, (0, 0))

            for i in range(len(drops)):
                text = random.choice(texts)
                win.blit(text, (i * self.font_p, drops[i] * self.font_p))
                drops[i] += 1
                if drops[i] * 10 > self.panel_height or random.random() > 0.95:
                    drops[i] = 0

            pygame.display.flip()


if __name__ == '__main__':

    test = CodeRain()
    test.play_code()
