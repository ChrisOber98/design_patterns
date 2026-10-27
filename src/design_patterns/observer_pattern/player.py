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
        self.rect.midbottom = self.window_handler.rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self) -> None:
        pygame.draw.rect(self.window_handler.surface, self.color, self.rect)
