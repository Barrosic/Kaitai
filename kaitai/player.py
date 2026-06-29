import pygame
from kaitai.entity import Entity
from kaitai.const import *
from kaitai.const import asset_path

class Player(Entity):
    def __init__(self):
        x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
        y = WINDOW_HEIGHT - PLAYER_HEIGHT - 20
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR)
        img = pygame.image.load(asset_path("images", "player.png"))
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < 0:
            self.x = 0
        if self.x > WINDOW_WIDTH - self.width:
            self.x - WINDOW_WIDTH - self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))