import pygame
import random
from config import *

class PowerUpManager:
    def __init__(self):
        self.powerups = []

    def spawn(self, position):
        powerup_type = random.choice(["E", "X2", "3X", "W", "Pew-Pew"])
        powerup_rect = pygame.Rect(position[0], position[1], POWERUP_WIDTH, POWERUP_HEIGHT)
        self.powerups.append((powerup_rect, powerup_type))

    def update(self, paddle):
        to_remove = []
        for powerup in self.powerups:
            powerup[0].y += 2
            if powerup[0].colliderect(paddle.rect):
                self.activate_powerup(powerup[1])
                to_remove.append(powerup)

        for powerup in to_remove:
            self.powerups.remove(powerup)

    def activate_powerup(self, powerup_type):
        if powerup_type == "E":
            print("Expanded Paddle Activated!")
        elif powerup_type == "X2":
            print("Double Paddle Activated!")
        elif powerup_type == "3X":
            print("Triple Balls Activated!")
        elif powerup_type == "W":
            print("Wrecking Ball Activated!")
        elif powerup_type == "Pew-Pew":
            print("Pew-Pew Bullets Activated!")

    def draw(self, screen):
        for powerup in self.powerups:
            pygame.draw.rect(screen, WHITE, powerup[0])
