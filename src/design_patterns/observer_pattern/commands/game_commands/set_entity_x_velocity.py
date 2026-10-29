from ...entities.entity import Entity
from ..command import Command


class SetEntityXVelocity(Command):
    def __init__(self, player: Entity, x_velocity: int) -> None:
        self.player: Entity = player
        self.x_velocity: int = x_velocity

    def execute(self) -> None:
        self.player.set_x_velocity(self.x_velocity)
