import pygame
import random
from config import *
from paddle import Paddle
from ball import Ball
from bricks import create_bricks
from powerups import PowerUpManager

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Initialize game objects
paddle = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10)
ball = Ball(WIDTH // 2, HEIGHT // 2)
bricks = create_bricks()
powerups = PowerUpManager()

clock = pygame.time.Clock()
running = True
lives = LIVES
score = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.move(keys)
    ball.move()
    ball.handle_collisions(paddle, bricks, powerups)

    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        pygame.draw.rect(screen, brick[1], brick[0])

    powerups.update(paddle)
    powerups.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
