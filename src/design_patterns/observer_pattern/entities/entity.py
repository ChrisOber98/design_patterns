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

    def set_x_y_position(
        self, x_pos: float | None = None, y_pos: float | None = None
    ) -> None:
        if x_pos != None:
            self.x = x_pos
        if y_pos != None:
            self.y = y_pos

        self.rect.x = self.x
        self.rect.y = self.y

    def reset_position(self) -> None:
        self.set_x_y_position(x_pos=0)

    def change_direction(self) -> None:
        cur_velocity = self.x_velocity
        cur_velocity *= -1
        self.x_velocity = cur_velocity
