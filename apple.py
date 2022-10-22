import pygame

from util.colors import Colors

class Apple:
    def __init__(self, size: int, x: int, y: int):
        self.size = size
        self.x = x
        self.y = y

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.rect(screen, Colors.RED, (self.x, self.y, self.size, self.size))