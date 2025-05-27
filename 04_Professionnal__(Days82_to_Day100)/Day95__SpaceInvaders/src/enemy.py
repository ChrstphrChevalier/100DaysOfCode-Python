import pygame
import os
import random

class Enemy:
    def __init__(self, x, y):
        color = random.choice(["red", "yellow", "green"])
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "assets", f"{color}.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = random.choice([-1, 1])
        self.speed = 3

    def move(self):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 40

    def draw(self, surface):
        surface.blit(self.image, self.rect)