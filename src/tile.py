import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
            self.hitbox = self.rect.copy()
            self.hitbox.update(self.rect.left, self.rect.top + 34, self.rect.width, self.rect.height - 44)
        else:
            self.rect = self.image.get_rect(topleft=pos)
            # Returns a new rectangle with the size changed by the given offset.
            # The rectangle remains centered around its current center.
            # Negative values will shrink the rectangle.
            self.hitbox = self.rect.inflate(0, -10)
