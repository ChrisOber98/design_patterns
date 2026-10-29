import pygame

from .commands.command_handler import Commandhandler
from .event_handler import EventHandler
from .entities.entity import Entity
from .window_handler import WindowHandler


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.window_handler: WindowHandler = WindowHandler()
        self.player: Entity = Entity(self.window_handler)
        self.clock: pygame.Clock = pygame.time.Clock()
        self.event_handler: EventHandler = EventHandler(self.player)
        self.command_handler: Commandhandler = Commandhandler()
        self.is_running: bool = True

    def run(self) -> None:
        while self.is_running:
            command = self.event_handler.process_input()
            if command:
                self.command_handler.add_command(command)
            self.command_handler.execute_commands()
            self.window_handler.update()
            self.player.update()
            self.player.draw()
            self.window_handler.draw()
            self.clock.tick(60)
