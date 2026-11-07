from ..entities.entity import Entity
from ..entities.fireball import Fireball
from ..gui.text_box import TextBox
from ..observer.events import Events
from ..observer.subject import Subject
from ..window_handler import WindowHandler


class PhysicsHandler(Subject):
    def __init__(
        self,
        window_handler: WindowHandler,
        entity_list: list[Entity] | None = None,
        text_boxs: list[TextBox] | None = None,
    ) -> None:
        Subject.__init__(self)
        if entity_list == None:
            self.entity_list = []
        else:
            self.entity_list: list[Entity] = entity_list

        if text_boxs == None:
            self.text_boxs = []
        else:
            self.text_boxs = text_boxs

        self.window_handler: WindowHandler = window_handler
        self._init_observers()

    def add_entity(self, entity: Entity) -> None:
        self.entity_list.append(entity)
        self.add_observer(entity)

    def add_text_box(self, text_box: TextBox) -> None:
        self.text_boxs.append(text_box)
        self.add_observer(text_box)

    def update(self) -> None:
        for entity in self.entity_list:
            self._update_entity_x_position(entity)
            self._update_entity_y_position(entity)
            self._check_for_edge_collision(entity)
            self._check_for_entity_collision()

    def _init_observers(self) -> None:
        for entity in self.entity_list:
            self.observers.append(entity)

        for text_box in self.text_boxs:
            self.text_boxs.append(text_box)

    def _update_entity_x_position(self, entity: Entity) -> None:
        entity.x += entity.x_velocity
        entity.x = max(entity.x, 0)
        entity.x = min(entity.x, self.window_handler.width - entity.width)
        entity.rect.x = entity.x

    def _update_entity_y_position(self, entity: Entity) -> None:
        entity.y -= entity.y_velocity
        entity.y = max(entity.y, 0)
        entity.y = min(entity.y, self.window_handler.height - entity.height)
        entity.rect.y = entity.y

        entity.y_velocity -= 1
        if entity.y == self.window_handler.height - entity.height:
            entity.y_velocity = 0

    def _check_for_edge_collision(self, entity: Entity) -> None:
        if entity.x >= self.window_handler.width - entity.width or entity.x <= 0:
            self.notify(entity, Events.EDGE_COLLISION)

    def _check_for_entity_collision(self) -> None:
        for i in range(len(self.entity_list)):
            for j in range(i + 1, len(self.entity_list)):
                if self.entity_list[i].rect.colliderect(self.entity_list[j]):
                    self.notify(self.entity_list[i], Events.PLAYER_COLLISION)
                    self.notify(self.entity_list[j], Events.PLAYER_COLLISION)
