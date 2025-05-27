import pygame
import os

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "assets", "bullet.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -7

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)