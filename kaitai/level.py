import pygame
from kaitai.const import *
from kaitai.entity_factory import EntityFactory
from kaitai.const import asset_path

class Level:

    def __init__(self):
        self.factory = EntityFactory()
        self.player = self.factory.create_player()
        self.bullets = []
        self.enemies = []
        self.last_spawn = 0
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        bg = pygame.image.load(asset_path("images", "bg_game.png"))
        self.background = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def shoot(self):
        bullet = self.factory.create_bullet(self.player)
        self.bullets.append(bullet)

    def update(self):
        # Player
        self.player.update()

        # Spawn de inimigos
        now = pygame.time.get_ticks()
        if now - self.last_spawn > ENEMY_INTERVAL:
            self.enemies.append(self.factory.create_enemy())
            self.last_spawn = now

        # Mover balas e inimigos
        for bullet in self.bullets:
            bullet.update()
        for enemy in self.enemies:
            enemy.update()

        # Mover balas que saíram da tela
        self.bullets = [b for b in self.bullets if b.y > 0]

        # Colisão bala x inimigo
        bullets_hit = set()
        enemies_hit = set()
        for i, bullet in enumerate(self.bullets):
            for j, enemy in enumerate(self.enemies):
                if bullet.rect.colliderect(enemy.rect):
                    bullets_hit.add(i)
                    enemies_hit.add(j)
        self.player.score += len(enemies_hit)

        # Colisão: inimigo × player (só se ainda não destruído)
        for i, enemy in enumerate(self.enemies):
            if i not in enemies_hit:
                if enemy.rect.colliderect(self.player.rect):
                    enemies_hit.add(i)
                    self.player.lives -= 1

        # Inimigos que passaram a tela (só se ainda não removidos)
        for i, enemy in enumerate(self.enemies):
            if i not in enemies_hit:
                if enemy.y >= WINDOW_HEIGHT:
                    enemies_hit.add(i)
                    self.player.lives -= 1

        # Filtra listas
        self.bullets = [b for i, b in enumerate(self.bullets) if i not in bullets_hit]
        self.enemies = [e for i, e in enumerate(self.enemies) if i not in enemies_hit]

        # Condições de fim
        if self.player.lives <= 0:
            self.player.lives = 0
            return STATE_GAMEOVER

        if self.player.score >= SCORE_TO_WIN:
            return STATE_VICTORY

        return STATE_PLAYING

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)

        # HUD
        score_text = self.font.render(f"Score: {self.player.score}", True, HUD_COLOR)
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, HUD_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WINDOW_WIDTH - 130, 10))