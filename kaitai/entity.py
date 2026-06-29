import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.width)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass