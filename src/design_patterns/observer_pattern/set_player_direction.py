from .command import Command
from .player import Player


class SetPlayerDirection(Command):
    def __init__(self, player: Player, direction: int):
        self.player = player
        self.direction = direction

    def execute(self):
        self.player.set_direction(self.direction)
