import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        # 0 => up
        # 1 => down
        # 2 => left
        # 3 => right
        direction = player.status_movement

        self.image = pygame.Surface((40, 40))

        if direction == 3:
            self.rect = self.image.get_rect(midleft=player.rect.midright)
        else:
            self.rect = self.image.get_rect(center=player.rect.center)
