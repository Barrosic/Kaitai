import random
from kaitai.player import Player
from kaitai.enemy import Enemy
from kaitai.bullet import Bullet
from kaitai.const import *

class EntityFactory:
    @staticmethod
    def create_player():
        return Player()

    @staticmethod
    def create_enemy():
        x = random.randint(0, WINDOW_WIDTH - ENEMY_WIDTH)
        return Enemy(x)

    @staticmethod
    def create_bullet(player):
        x = player.x + player.width // 2 - BULLET_WIDTH // 2
        y = player.y
        return Bullet(x, y)