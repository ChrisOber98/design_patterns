from abc import ABC

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class TextBox(ABC):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        color: tuple[int, int, int] = (0, 0, 0),
        text: str | None = None,
    ):
        self.font: Font = pygame.font.Font(None, 36)
        self.x: float = x
        self.y: float = y
        self.color: tuple[int, int, int] = color
        self.surface: Surface = None
        self.rect: Rect = None
        if text:
            self.render(text)

    def render(self, text: str) -> None:
        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
