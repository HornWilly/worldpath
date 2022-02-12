import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        # Returns a new rectangle with the size changed by the given offset.
        # The rectangle remains centered around its current center.
        # Negative values will shrink the rectangle.
        self.hitbox = self.rect.inflate(0, -10)
