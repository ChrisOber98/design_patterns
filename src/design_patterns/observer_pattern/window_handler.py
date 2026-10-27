import pygame


class WindowHandler:
    def __init__(self, window_width: int = 800, window_height: int = 600) -> None:
        self.width = window_width
        self.height = window_height
        self.bg_color = (255, 255, 255)
        self.surface = self._create_surface()
        self.rect = self.surface.get_rect()

    def display(self) -> None:
        self._update()
        self._draw()

    def _update(self) -> None:
        self._set_bg_color()

    def _draw(self) -> None:
        pygame.display.flip()

    def _create_surface(self) -> None:
        return pygame.display.set_mode((self.width, self.height))

    def _set_bg_color(self) -> None:
        self.surface.fill(self.bg_color)
