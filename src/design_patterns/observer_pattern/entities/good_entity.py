from ..window_handler import WindowHandler
from .entity import Entity


class GoodEntity(Entity):
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (255, 0, 0),
        width: float = 20,
        height: float = 20,
    ):
        super().__init__(window_handler, color, width, height)
        self.rect.bottomright = self.window_handler.rect.bottomright
        self.x = self.rect.x
        self.y = self.rect.y
