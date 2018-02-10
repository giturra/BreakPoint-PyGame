import pygame
import sys
from Table import Block
from pygame.locals import *


class Game(object):
    def __init__(self, width=400, height=300):

        self.title = 'BreakPoint'
        self.width = width
        self.height = height
        self.surface = None

    def start_game(self):
        pygame.init()
        size = (self.width, self.height)
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(self.title)
        print(self.surface)

        block = Block()

        while True:
            for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
            self.surface.blit(block.image, (self.width/2.0 - 100, self.height - 50))
            pygame.display.flip()


if __name__ == '__main__':
    game = Game(600, 400)
    game.start_game()
