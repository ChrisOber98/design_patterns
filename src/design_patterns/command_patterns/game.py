import pygame

from .player import Player
from .event_handler import EventHandler

from .game_commands import UndoMoveCommand


class Game:
    def __init__(self):
        pygame.init()

        self.event_handler = EventHandler()

        self.screen = pygame.display.set_mode((900, 900))
        self.clock = pygame.time.Clock()

        self.player = Player(self)

        self.command_list = []

    def run(self):
        while True:
            self.screen.fill("purple")
            self.player.draw()

            command = self.event_handler.handle_input()

            if command:
                ret = command.execute(self.player, self.command_list)
                print(ret)
                if ret:
                    self.command_list.append(command)

            pygame.display.flip()
            # print(f"x:{self.player.x} y:{self.player.y}")
            self.clock.tick(60)
