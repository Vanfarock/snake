import pygame

from util.events import Event

class KeyboardHandler:
    def __init__(self):
        self.actions = {
            pygame.K_d: Event.MOVE_RIGHT,
            pygame.K_a: Event.MOVE_LEFT,
            pygame.K_w: Event.MOVE_UP,
            pygame.K_s: Event.MOVE_DOWN,
            pygame.K_RIGHT: Event.MOVE_RIGHT,
            pygame.K_LEFT: Event.MOVE_LEFT,
            pygame.K_UP: Event.MOVE_UP,
            pygame.K_DOWN: Event.MOVE_DOWN,
            pygame.K_RETURN: Event.RESET,
            pygame.K_KP_ENTER: Event.RESET,
        }

    def handle(self, key: str):
        return self.actions.get(key, None)