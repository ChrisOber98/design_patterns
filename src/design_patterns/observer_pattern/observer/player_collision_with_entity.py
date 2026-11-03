from .events import Events
from .observer import Observer

from ..entities.entity import Entity


class PlayerCollisionWithEntity(Observer):
    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.PLAYER_COLLISION:
                print("We hit")
            case _:
                pass
