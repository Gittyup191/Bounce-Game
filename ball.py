import pygame
import random
from config import *

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = -BALL_SPEED

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def handle_collisions(self, paddle, bricks, powerups):
        if self.rect.colliderect(paddle.rect):
            self.speed_y *= -1

        for brick in bricks[:]:
            if self.rect.colliderect(brick[0]):
                bricks.remove(brick)
                self.speed_y *= -1
                if brick[2]:  # Has power-up
                    powerups.spawn(brick[0].center)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)
