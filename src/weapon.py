import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status_to_animation[player.status_movement]

        image_path = f'../graphics/weapons/{player.get_weapon()}/{direction}.png'
        self.image = pygame.image.load(image_path).convert_alpha()

        # pygame.math.Vector2(x, y) -> We want weapon to be exactly where player's arm is
        if direction == "up":
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))
        elif direction == "down":
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))
        elif direction == "left":
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        else:  # right
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
