import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        # 0 => up
        # 1 => down
        # 2 => left
        # 3 => right
        direction = player.status_movement

        image_path = f'../graphics/weapons/{player.weapon}/{player.status_to_animation[direction]}.png'
        self.image = pygame.image.load(image_path).convert_alpha()

        # pygame.math.Vector2(x, y) -> We want weapon to be exactly where player's arm is
        if direction == 0:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))
        elif direction == 1:
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))
        elif direction == 2:
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        else:
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
