from random import choice

from camera import Camera
from debug import debug
from player import Player
from settings import *
from tile import Tile
from utils import *
from weapon import Weapon


class Level:
    def __init__(self):
        self.player = None

        # sprite group setup
        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': get_layout_from_csv('../map/map_floor_blocks.csv'),
            'grass': get_layout_from_csv('../map/map_grass.csv'),
            'objects': get_layout_from_csv('../map/map_objects.csv'),
        }
        graphics = {
            'grass': get_files_list_from_folder('../graphics/grass'),
            'objects': get_files_list_from_folder('../graphics/objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'objects':
                            object_image = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', object_image)

        self.player = Player((2000, 1420), [self.visible_sprites], self.obstacle_sprites, self.create_attack)

    def create_attack(self):
        Weapon(self.player, [self.visible_sprites])

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.get_status())
