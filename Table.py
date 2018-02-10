import pygame

class Block(pygame.sprite.Sprite):


    def __init__(self):


        super(Block, self).__init__()
        self.image = pygame.Surface((200, 50))
        self.image.fill(pygame.Color('red'))

        self.rect = self.image.get_rect()
        print(self.rect)
