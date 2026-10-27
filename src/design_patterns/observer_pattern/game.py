import pygame

from .event_handler import EventHandler
from .window_handler import WindowHandler


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler()
        self.window_handler = WindowHandler()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.event_handler.process_input()
            self.window_handler.display()
            self.clock.tick(60)
