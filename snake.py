import pygame

from util.colors import Colors
from util.vector import Vector

class Snake:
    def __init__(self, size: int, x: int, y: int):
        self.size = size
        self.x = x
        self.y = y
        self.last_x = None
        self.last_y = None
        self.tail = []

    def move(self, direction: Vector):
        for i in list(reversed(range(len(self.tail)))):
            if i - 1 >= 0:
                self.tail[i] = self.tail[i - 1]
            else:
                self.tail[i] = (self.x, self.y)

        self.last_x = self.x
        self.last_y = self.y
        self.x += direction.x
        self.y += direction.y

    def grow(self):
        self.tail.append((self.last_x, self.last_y))

    def is_inside(self, x: int, y: int):
        if x == self.x and y == self.y:
            return True

        for (tail_x, tail_y) in self.tail:
            if tail_x == x and tail_y == y:
                return True
        return False

    def is_inside_itself(self):
        for (x, y) in self.tail:
            if x == self.x and y == self.y:
                return True
        return False

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.rect(screen, Colors.DARK_GREEN, (self.x, self.y, self.size, self.size))
        for tail in self.tail:
            x, y = tail
            pygame.draw.rect(screen, Colors.GREEN, (x, y, self.size, self.size))