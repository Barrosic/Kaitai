import pygame
from kaitai.entity import Entity
from kaitai.const import *
from kaitai.const import asset_path

class Enemy(Entity):
    def __init__(self, x):
        super().__init__(x, -ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_COLOR)
        img = pygame.image.load(asset_path("images", "enemy.png"))
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.speed = ENEMY_SPEED

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))