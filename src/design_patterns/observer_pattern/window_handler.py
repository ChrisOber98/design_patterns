import pygame

from .entities.entity import Entity
from .gui.text_box import TextBox


class WindowHandler:
    def __init__(
        self,
        window_width: int = 800,
        window_height: int = 600,
        entitys: list[Entity] | None = None,
        text_boxs: list[TextBox] | None = None,
    ) -> None:
        if entitys == None:
            self.entitys = []
        else:
            self.entitys = entitys
        if text_boxs == None:
            self.text_boxs = []
        else:
            self.text_boxs = text_boxs
        self.width = window_width
        self.height = window_height
        self.bg_color = (255, 255, 255)
        self.surface = self._create_surface()
        self.rect = self.surface.get_rect()

    def add_entity(self, entity: Entity) -> None:
        self.entitys.append(entity)

    def add_textbox(self, text_box: TextBox) -> None:
        self.text_boxs.append(text_box)

    def _update(self) -> None:
        self._set_bg_color()

    def draw(self) -> None:
        self._update()
        for entity in self.entitys:
            pygame.draw.rect(self.surface, entity.color, entity.rect)
        for text_box in self.text_boxs:
            self.surface.blit(text_box.surface, text_box.rect)

        pygame.display.flip()

    def _create_surface(self) -> None:
        return pygame.display.set_mode((self.width, self.height))

    def _set_bg_color(self) -> None:
        self.surface.fill(self.bg_color)
