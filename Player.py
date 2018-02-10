import pygame

class Block(pygame.sprite.Sprite):


    def __init__(self, window_size):


        super(Block, self).__init__()
        self.initialize = True
        self.x = 200
        self.y = 50
        self.window_size = window_size
        self.image = pygame.Surface((self.x, self.y))
        self.image.fill(pygame.Color('red'))

        self.rect = self.image.get_rect()
        print(self.rect)


    def handle_keys(self):


        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.x += dist
        if key[pygame.K_RIGHT]:
            self.x -= dist




    def draw(self, surface):
        if self.initialize:
            surface.blit(self.image, (self.window_size[0]/2.0 - self.x / 2.0, self.window_size[1] - self.y))
            self.initialize = False
        else:
            surface.blit(self.image, (0, 0))
