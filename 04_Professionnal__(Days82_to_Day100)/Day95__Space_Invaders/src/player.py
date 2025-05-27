import pygame
import os
from src.bullet import Bullet

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "assets", "player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen_width // 2, screen_height - 10)
        self.screen_width = screen_width
        self.speed = 5
        self.last_shot = 0
        self.shot_cooldown = 500  # ms

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.right < self.screen_width:
            self.rect.x += self.speed

    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shot > self.shot_cooldown

    def shoot(self):
        self.last_shot = pygame.time.get_ticks()
        return Bullet(self.rect.centerx, self.rect.top)

    def draw(self, surface):
        surface.blit(self.image, self.rect)