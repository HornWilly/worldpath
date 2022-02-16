# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64
PLAYER_SPEED = 5
PLAYER_ATTACK_COOLDOWN_MS = 400
PLAYER_ANIMATION_SPEED = 0.15
WEAPON_SWITCH_COOLDOWN_MS = 200

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graphics/weapons/sai/full.png'}
}
