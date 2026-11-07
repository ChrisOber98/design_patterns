import pygame

from .commands.command_handler import Commandhandler
from .entities.fireball import Fireball
from .entities.player import Player
from .event_handler import EventHandler
from .gui.scoreboard import Scoreboard
from .gui.info_box import InfoBox
from .physics.physics_handler import PhysicsHandler
from .window_handler import WindowHandler


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.window_handler: WindowHandler = WindowHandler()
        self.physicsHandler: PhysicsHandler = PhysicsHandler(self.window_handler)
        self.player: Player = Player(
            window_handler=self.window_handler,
            x=self.window_handler.width / 2,
            y=self.window_handler.height,
        )
        self.physicsHandler.add_entity(self.player)
        self.window_handler.add_entity(self.player)
        self.fireball: Fireball = Fireball(
            self.window_handler, x=0, y=self.window_handler.height
        )
        self.physicsHandler.add_entity(self.fireball)
        self.window_handler.add_entity(self.fireball)
        self.clock: pygame.Clock = pygame.time.Clock()
        self.event_handler: EventHandler = EventHandler(self.player)
        self.command_handler: Commandhandler = Commandhandler()
        self.is_running: bool = True
        self.score_board: Scoreboard = Scoreboard(10, 0, (0, 255, 0), "Score: 0")
        self.window_handler.add_textbox(self.score_board)
        self.physicsHandler.add_text_box(self.score_board)
        self.info_box: InfoBox = InfoBox(580, 0)
        self.window_handler.add_textbox(self.info_box)

        self.fireball.set_x_velocity(10)

    def run(self) -> None:
        while self.is_running:
            command = self.event_handler.process_input()
            if command:
                self.command_handler.add_command(command)
            self.command_handler.execute_commands()
            self.physicsHandler.update()
            self.window_handler.draw()
            self.clock.tick(60)
