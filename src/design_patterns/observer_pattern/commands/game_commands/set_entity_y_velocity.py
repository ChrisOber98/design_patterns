from ...entities.entity import Entity
from ..command import Command


class SetEntityYVelocity(Command):
    def __init__(self, player: Entity, y_velocity: int) -> None:
        self.player: Entity = player
        self.y_velocity: int = y_velocity

    def execute(self) -> None:
        self.player.set_y_velocity(self.y_velocity)
