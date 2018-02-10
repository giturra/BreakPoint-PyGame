import pygame
import sys
from Player import Block
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

        block = Block((self.width, self.height))

        while True:
            for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
            block.draw(self.surface)
            block.handle_keys()
            pygame.display.flip()
            pygame.display.update()


if __name__ == '__main__':
    game = Game(600, 400)
    game.start_game()
