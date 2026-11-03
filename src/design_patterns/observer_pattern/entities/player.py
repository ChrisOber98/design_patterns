from ..observer.events import Events
from ..observer.observer import Observer
from ..window_handler import WindowHandler
from .entity import Entity


class Player(Entity, Observer):
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (0, 0, 0),
        width: float = 20,
        height: float = 20,
        x: float = 0,
        y: float = 0,
    ):
        Observer.__init__(self)
        Entity.__init__(self, color, width, height, x, y)
        self.health: int = 50

    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.EDGE_COLLISION:
                pass
            case Events.PLAYER_COLLISION:
                pass
