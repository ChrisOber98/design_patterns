import pygame
from pygame import Rect

from .window_handler import WindowHandler


class Player:
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (0, 0, 0),
        width: float = 20,
        height: float = 20,
    ):
        self.window_handler: WindowHandler = window_handler
        self.color: tuple[int, int, int] = color
        self.width: float = width
        self.height: float = height
        self.x: float = 0
        self.y: float = 0
        self.rect: Rect = Rect(self.x, self.y, self.width, self.height)
        self.direction: int = 0
        self.speed: int = 5
        self.rect.midbottom = self.window_handler.rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self) -> None:
        self.x += self.direction * self.speed
        self.x = max(self.x, 0)
        self.x = min(self.x, self.window_handler.width - self.width)
        self.rect.x = self.x

    def draw(self) -> None:
        pygame.draw.rect(self.window_handler.surface, self.color, self.rect)

    def set_direction(self, direction: int) -> None:
        self.direction = direction
