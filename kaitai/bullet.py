import pygame
from kaitai.entity import Entity
from kaitai.const import *
from kaitai.const import asset_path

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, BULLET_COLOR)
        img = pygame.image.load(asset_path("images", "bullet.png"))
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.speed = BULLET_SPEED

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))