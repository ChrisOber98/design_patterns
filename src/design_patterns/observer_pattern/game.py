import pygame

from .event_handler import EventHandler


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.event_handler.process_input()
            self.screen.fill("white")
            pygame.display.flip()
            self.clock.tick(60)
