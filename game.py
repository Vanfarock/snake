import random
import pygame
from apple import Apple
from util.events import Event
from handlers.keyboard_handler import KeyboardHandler
from snake import Snake

from util.colors import Colors
from util.vector import Vector

MAX_FPS = 60

current_fps = MAX_FPS

class Game:
    def __init__(self, width: int, height: int):
        self.running: bool = True
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.keyboard_handler = KeyboardHandler()
        self.reset()

    def reset(self):
        self.end_game = False
        self.win = False
        self.max_apples = 3
        self.apples = []
        self.ticks = 0
        self.action = None
        self.last_action = None
        self.cell_size = self.height / 10
        self.snake = Snake(self.cell_size, 0, 0)
        self.snake_move_delay = 200
        self.generate_apples()

    def run(self):
        pygame.init()
        pygame.font.init()

        while self.running:
            self.ticks += self.clock.tick(MAX_FPS)
            
            self.screen.fill(Colors.BLACK)
            
            self.check_events()

            self.update()

            self.draw()

            pygame.display.flip()

        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.action = self.keyboard_handler.handle(event.key)
                if not Event.is_move(self.action) and not self.end_game:
                    self.action = self.last_action

                if Event.are_opposites(self.action, self.last_action):
                    self.action = self.last_action

    def update(self):
        if self.snake_is_out_of_board() or self.snake.is_inside_itself():
            self.end_game = True
            self.win = False

        if Event.is_move(self.action) and self.snake_can_move():
            direction = self.get_directions()[self.action]
            direction.x *= self.cell_size
            direction.y *= self.cell_size
            self.snake.move(direction)
            self.ticks = 0
            self.last_action = self.action

        eaten_apple = self.will_eat_apple()
        if eaten_apple is not None:
            self.apples.remove(eaten_apple)
            self.generate_apples()
            self.snake.grow()

        if Event.is_reset(self.action) and self.end_game:
            self.reset()

    def snake_is_out_of_board(self):
        if self.snake.x < 0 or self.snake.x >= self.width:
            return True
        if self.snake.y < 0 or self.snake.y >= self.height:
            return True
        return False

    def snake_can_move(self):
        return self.ticks > self.snake_move_delay

    def get_directions(self) -> 'dict[str, Vector]':
        return {
            Event.MOVE_UP: Vector(0, -1),
            Event.MOVE_DOWN: Vector(0, 1),
            Event.MOVE_LEFT: Vector(-1, 0), 
            Event.MOVE_RIGHT: Vector(1, 0)
        }

    def will_eat_apple(self) -> Apple:
        eaten_apple = None
        for apple in self.apples:
            if apple.x == self.snake.x and apple.y == self.snake.y:
                eaten_apple = apple
                break

        return eaten_apple

    def generate_apples(self):
        while len(self.apples) < self.max_apples:
            horizontal_cells = round(self.width / self.cell_size)
            vertical_cells = round(self.height / self.cell_size)
            x = random.randint(0, horizontal_cells - 1) * self.cell_size
            y = random.randint(0, vertical_cells - 1) * self.cell_size

            if self.snake.is_inside(x, y):
                continue

            self.apples.append(Apple(self.cell_size, x, y))

    def draw(self):
        if self.end_game:
            self.draw_result()
            return

        self.snake.draw(self.screen)
        
        for apple in self.apples:
            apple.draw(self.screen)

        self.draw_board_lines()

    def draw_result(self):
        font = pygame.font.SysFont('Comic Sans MS', 50)
        message = 'You lost'
        if self.win:
            message = 'You win'
        surface = font.render(message, False, Colors.WHITE)
        
        x, y = self.width / 2 - surface.get_width() / 2, self.height / 2 - surface.get_height() / 2
        self.screen.blit(surface, (x, y))

    def draw_board_lines(self):
        horizontal_cells = round(self.width / self.cell_size)
        for x in range(1, horizontal_cells):
            pygame.draw.line(
                self.screen,
                Colors.WHITE,
                (x * self.cell_size, 0),
                (x * self.cell_size, self.width))

        vertical_cells = round(self.height / self.cell_size)
        for y in range(1, vertical_cells):
            pygame.draw.line(
                self.screen,
                Colors.WHITE,
                (0, y * self.cell_size),
                (self.width, y * self.cell_size))
