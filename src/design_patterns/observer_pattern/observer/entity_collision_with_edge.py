from .events import Events
from .observer import Observer

from ..entities.entity import Entity


class EntityCollisionWithEdge(Observer):
    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.EDGE_COLLISION:
                print("EDGE hit")
            case _:
                pass
