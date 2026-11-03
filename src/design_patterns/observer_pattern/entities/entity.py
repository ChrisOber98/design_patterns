from abc import ABC

from pygame.rect import Rect


class Entity(ABC):
    def __init__(
        self,
        color: tuple[int, int, int] = (0, 0, 0),
        width: float = 20,
        height: float = 20,
        x: float = 0,
        y: float = 0,
        x_velocity: int = 0,
    ) -> None:
        self.color: tuple[int, int, int] = color
        self.width: float = width
        self.height: float = height
        self.x: float = x
        self.y: float = y
        self.rect: Rect = Rect(self.x, self.y, self.width, self.height)
        self.x_velocity: int = x_velocity
        self.y_velocity: int = 0
        self.speed: int = 5

        self.x = self.rect.x
        self.y = self.rect.y

    def set_x_velocity(self, x_velocity: int) -> None:
        self.x_velocity = x_velocity

    def set_y_velocity(self, y_velocity: int) -> None:
        self.y_velocity = y_velocity
