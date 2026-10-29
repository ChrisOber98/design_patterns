from abc import ABC, abstractmethod

import pygame
from pygame import Rect

from ..window_handler import WindowHandler


class Entity(ABC):
    def __init__(
        self,
        window_handler: WindowHandler,
        color: tuple[int, int, int] = (0, 0, 0),
        width: float = 20,
        height: float = 20,
    ) -> None:
        self.window_handler: WindowHandler = window_handler
        self.color: tuple[int, int, int] = color
        self.width: float = width
        self.height: float = height
        self.x: float = 0
        self.y: float = 0
        self.rect: Rect = Rect(self.x, self.y, self.width, self.height)
        self.x_velocity: int = 0
        self.y_velocity: int = 0
        self.rect.midbottom = self.window_handler.rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self) -> None:
        self.x += self.x_velocity
        self.x = max(self.x, 0)
        self.x = min(self.x, self.window_handler.width - self.width)
        self.rect.x = self.x

        self.y -= self.y_velocity
        self.y = max(self.y, 0)
        self.y = min(self.y, self.window_handler.height - self.height)
        self.rect.y = self.y

        self.y_velocity -= 1
        if self.y == self.window_handler.height - self.height:
            self.y_velocity = 0

    def draw(self) -> None:
        pygame.draw.rect(self.window_handler.surface, self.color, self.rect)

    def set_x_velocity(self, x_velocity: int) -> None:
        self.x_velocity = x_velocity

    def set_y_velocity(self, y_velocity: int) -> None:
        self.y_velocity = y_velocity
