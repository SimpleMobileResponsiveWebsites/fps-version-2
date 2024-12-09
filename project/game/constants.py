"""Game-wide constants"""

# Physics
GRAVITY = -9.81
JUMP_FORCE = 5.0

# Collision masks
GROUND_MASK = 1
PLAYER_MASK = 2
PROJECTILE_MASK = 4

# Game settings
MAX_FPS = 60
TICK_RATE = 1.0 / MAX_FPS