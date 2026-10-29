from ..window_handler import WindowHandler
from .entity import Entity


class Player(Entity):
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (0, 0, 0),
        width: float = 20,
        height: float = 20,
    ):
        super().__init__(window_handler, color, width, height)
        self.health: int = 50
