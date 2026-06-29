import pygame
import sys
from kaitai.const import *
from kaitai.menu import Menu
from kaitai.level import Level
from kaitai.const import asset_path

class Game:

    def __init__(self):
        pygame.init()
        self.screen     = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock      = pygame.time.Clock()
        self.state      = STATE_MENU
        self.menu       = Menu()
        self.level      = None
        self.last_score = 0
        pygame.display.set_caption(TITLE)
        pygame.mixer.init()
        pygame.mixer.music.load(asset_path("sounds", "bgs_game.wav"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        bg = pygame.image.load(asset_path("images", "bg_game.png"))
        self.background = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        running = True

        while running:

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.state == STATE_MENU:
                        if event.key == pygame.K_RETURN:
                            self.level = Level()
                            self.state = STATE_PLAYING

                    elif self.state == STATE_PLAYING:
                        if event.key == pygame.K_SPACE:
                            self.level.shoot()

                    elif self.state in (STATE_GAMEOVER, STATE_VICTORY):
                        if event.key == pygame.K_r:
                            self.level = Level()
                            self.state = STATE_PLAYING

            # Atualizações
            if self.state == STATE_PLAYING:
                self.state = self.level.update()
                if self.state != STATE_PLAYING:
                    self.last_score = self.level.player.score

            # Desenhos
            self.screen.blit(self.background, (0, 0))

            if self.state == STATE_MENU:
                self.menu.draw_menu(self.screen)
            elif self.state == STATE_PLAYING:
                self.level.draw(self.screen)
            elif self.state == STATE_GAMEOVER:
                self.menu.draw_gameover(self.screen, self.last_score)
            elif self.state == STATE_VICTORY:
                self.menu.draw_victory(self.screen, self.last_score)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()