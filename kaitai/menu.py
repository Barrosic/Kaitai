import pygame
from kaitai.const import *

class Menu:
    def __init__(self):
        self.font_title = pygame.font.SysFont(None, 64)
        self.font_sub   = pygame.font.SysFont(None, 32)

    def _draw_centered(self, screen, text, font, color, y):
        rendered = font.render(text, True, color)
        x = (WINDOW_WIDTH - rendered.get_width()) // 2
        screen.blit(rendered, (x, y))

    def draw_menu(self, screen):
        self._draw_centered(screen, "KAITAI",                      self.font_title, COLOR_WHITE, 160)
        self._draw_centered(screen, "< > Mover  |  SPACE Atirar",  self.font_sub,   COLOR_WHITE, 280)
        self._draw_centered(screen, "ENTER para comecar",           self.font_sub,   COLOR_WHITE, 340)

    def draw_gameover(self, screen, score):
        self._draw_centered(screen, "GAME OVER",                   self.font_title, COLOR_RED,   180)
        self._draw_centered(screen, f"Score: {score}",             self.font_sub,   COLOR_WHITE, 290)
        self._draw_centered(screen, "R para jogar novamente",      self.font_sub,   COLOR_WHITE, 340)

    def draw_victory(self, screen, score):
        self._draw_centered(screen, "VITORIA!",                    self.font_title, COLOR_GREEN, 180)
        self._draw_centered(screen, f"Score: {score}",             self.font_sub,   COLOR_WHITE, 290)
        self._draw_centered(screen, "R para jogar novamente",      self.font_sub,   COLOR_WHITE, 340)