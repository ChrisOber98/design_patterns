import pygame

from .entities.entity import Entity


class WindowHandler:
    def __init__(
        self,
        window_width: int = 800,
        window_height: int = 600,
        entity_list: list[Entity] | None = None,
    ) -> None:
        if entity_list == None:
            self.entity_list = []
        else:
            self.entity_list = entity_list
        self.width = window_width
        self.height = window_height
        self.bg_color = (255, 255, 255)
        self.surface = self._create_surface()
        self.rect = self.surface.get_rect()

    def add_entity(self, entity: Entity) -> None:
        self.entity_list.append(entity)

    def _update(self) -> None:
        self._set_bg_color()

    def draw(self) -> None:
        self._update()
        for entity in self.entity_list:
            pygame.draw.rect(self.surface, entity.color, entity.rect)
        pygame.display.flip()

    def _create_surface(self) -> None:
        return pygame.display.set_mode((self.width, self.height))

    def _set_bg_color(self) -> None:
        self.surface.fill(self.bg_color)
