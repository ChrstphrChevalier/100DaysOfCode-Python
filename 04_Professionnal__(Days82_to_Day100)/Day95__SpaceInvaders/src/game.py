import pygame
import sys
import random
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()

        self.player = Player(self.WIDTH, self.HEIGHT)
        self.enemies = [Enemy(random.randint(0, self.WIDTH - 64), random.randint(50, 150)) for _ in range(6)]
        self.bullets = []

        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.lives = 3
        self.running = True

    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (self.WIDTH - 120, 10))

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.enemies.append(Enemy(random.randint(0, self.WIDTH - 64), random.randint(50, 150)))
                    self.score += 10
                    break

    def check_enemy_reach_bottom(self):
        for enemy in self.enemies:
            if enemy.rect.y >= self.HEIGHT - 64:
                self.lives -= 1
                self.enemies.remove(enemy)
                self.enemies.append(Enemy(random.randint(0, self.WIDTH - 64), random.randint(50, 150)))
                if self.lives <= 0:
                    self.running = False

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move_left()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()
            if keys[pygame.K_SPACE]:
                if self.player.can_shoot():
                    bullet = self.player.shoot()
                    self.bullets.append(bullet)

            for bullet in self.bullets[:]:
                bullet.move()
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)

            self.check_collisions()
            self.check_enemy_reach_bottom()

            self.player.draw(self.screen)
            for bullet in self.bullets:
                bullet.draw(self.screen)
            for enemy in self.enemies:
                enemy.move()
                enemy.draw(self.screen)

            self.draw_ui()
            pygame.display.flip()

        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        self.screen.blit(game_over_text, (self.WIDTH//2 - 80, self.HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()