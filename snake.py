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
        self.last_tail_x = None
        self.last_tail_y = None

    def move(self, direction: Vector):
        for i in list(reversed(range(len(self.tail)))):
            if i - 1 < 0:
                self.tail[i] = (self.x, self.y)
            else:
                self.tail[i] = self.tail[i - 1]

            if i == len(self.tail) - 1:
                self.last_tail_x = self.tail[i][0]
                self.last_tail_y = self.tail[i][1]

        self.last_x = self.x
        self.last_y = self.y
        self.x += direction.x
        self.y += direction.y

    def grow(self):
        if self.last_tail_x is not None and self.last_tail_y is not None:
            self.tail.append((self.last_x, self.last_y))
        else:
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
        t = 0.0

        color = Colors.lerp(Colors.GREEN, Colors.DARK_BLUE, t)
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

        if len(self.tail) == 0:
            return

        t_change = 1 / len(self.tail)
        for tail in self.tail:
            t += t_change
            x, y = tail
            color = Colors.lerp(Colors.GREEN, Colors.DARK_BLUE, t)
            pygame.draw.rect(screen, color, (x, y, self.size, self.size))

    