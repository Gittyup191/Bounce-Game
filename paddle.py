import pygame
from config import *

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - PADDLE_WIDTH:
            self.rect.x += PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
