from re import X
import pygame as pg
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x,y))

shape = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']

class Blocks:
    def __init__(self):
        self.shape = shape
        self.block_size = 6
        self.blocks = pg.sprite.Group()
        self.create_obstacle()

    def create_obstacle(self):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = col_index*self.block_size
                    y = row_index*self.block_size
                    block = Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)
    