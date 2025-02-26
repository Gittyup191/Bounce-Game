import pygame
import random
from config import *

def create_bricks():
    bricks = []
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    powerup_positions = random.sample(range(BRICK_ROWS * BRICK_COLS), 5)

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick_x = col * BRICK_WIDTH
            brick_y = row * BRICK_HEIGHT
            brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_color = colors[row]
            has_powerup = (row * BRICK_COLS + col) in powerup_positions
            bricks.append((brick_rect, brick_color, has_powerup))
    
    return bricks
