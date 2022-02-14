import pygame


class Camera(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        # creating the ground
        self.ground_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # Center camera on player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the ground
        ground_offset_pos = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset_pos)

        # Sort all sprites by Y axes
        # More a sprite is on top and more this sprite is on background against a sprite on bottom
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
