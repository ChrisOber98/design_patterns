import pygame

from player import Player
from event_handler import EventHandler


class Game:
    def __init__(self):
        pygame.init()

        self.event_handler = EventHandler()

        self.screen = pygame.display.set_mode((900, 900))
        self.clock = pygame.time.Clock()

        self.player = Player(self)

    def run(self):
        while True:
            self.screen.fill("purple")
            self.player.draw()

            command = self.event_handler.handle_input()

            if command:
                command.execute(command, self.player)

            pygame.display.flip()
            self.clock.tick(60)
