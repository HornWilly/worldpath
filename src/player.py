import pygame

from settings import *
from utils import *
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, create_weapon, destroy_weapon):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # graphics setup
        self.animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': [],
            'right_attack': [],
            'left_attack': [],
            'up_attack': [],
            'down_attack': []
        }
        self.status_to_animation = [
            'up',
            'down',
            'left',
            'right',
            'up_idle',
            'down_idle',
            'left_idle',
            'right_idle',
            'up_attack',
            'down_attack',
            'left_attack',
            'right_attack',
        ]
        self.import_player_assets()
        self.status_movement = 1
        self.status_action = 0
        self.frame_index = 0
        self.animation_speed = PLAYER_ANIMATION_SPEED

        # movement
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.attacking = False
        self.attack_cooldown = PLAYER_ATTACK_COOLDOWN_MS
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        # weapons setup
        self.create_weapon = create_weapon
        self.destroy_weapon = destroy_weapon
        self.weapon_index = 0
        self.nb_weapon = len(list(weapon_data.keys()))
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_duration_cooldown = WEAPON_SWITCH_COOLDOWN_MS

    def import_player_assets(self):
        character_path = '../graphics/player/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = get_files_list_from_folder(full_path)

    def input(self):
        # Get user control when player is not attacking
        if not self.attacking:
            keys = pygame.key.get_pressed()

            # movement input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status_movement = 0
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status_movement = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status_movement = 3
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status_movement = 2
            else:
                self.direction.x = 0

            # attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.status_action = 1
                self.create_weapon()

            # magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.status_action = 1

            if keys[pygame.K_BACKSPACE] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                self.weapon_index += 1
                self.weapon_index = self.weapon_index % self.nb_weapon

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0 and self.status_action == 0:
            return self.status_to_animation[self.status_movement + 4]

        # attack status
        if self.status_action == 1:
            return self.status_to_animation[self.status_movement + 8]
        else:
            return self.status_to_animation[self.status_movement]

    def get_weapon(self):
        return list(weapon_data.keys())[self.weapon_index]

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.check_collision_horizontal()
        self.hitbox.y += self.direction.y * speed
        self.check_collision_vertical()
        # We move the rect center to be equal to hitbox center
        # Rect is where displayed the player's sprite
        self.rect.center = self.hitbox.center

    def check_collision_horizontal(self):
        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.x > 0:  # moving right
                    self.hitbox.right = sprite.hitbox.left
                if self.direction.x < 0:  # moving left
                    self.hitbox.left = sprite.hitbox.right

    def check_collision_vertical(self):
        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.y > 0:  # moving down
                    self.hitbox.bottom = sprite.hitbox.top
                if self.direction.y < 0:  # moving up
                    self.hitbox.top = sprite.hitbox.bottom

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.status_action = 0
                self.destroy_weapon()
            else:
                # On attack, stop all player's movement
                self.direction.x = 0
                self.direction.y = 0

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.weapon_switch_duration_cooldown:
                self.can_switch_weapon = True

    def animate(self):
        animation = self.animations[self.get_status()]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        # Order is important
        self.input()
        self.cooldown()
        self.animate()
        self.move(self.speed)
