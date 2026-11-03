from ..observer.observer import Observer
from ..window_handler import WindowHandler
from .entity import Entity

from ..observer.events import Events


class Fireball(Entity, Observer):
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (255, 0, 0),
        width: float = 20,
        height: float = 20,
        x: float = 0,
        y: float = 0,
        x_velocity: int = 0,
    ):
        Entity.__init__(
            self, color=color, width=width, height=height, x=x, y=y, x_velocity=-10
        )
        Observer.__init__(self)

    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.EDGE_COLLISION:
                cur_velocity = self.x_velocity
                cur_velocity *= -1
                self.x_velocity = cur_velocity
            case Events.PLAYER_COLLISION:
                pass
