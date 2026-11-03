from abc import ABC, abstractmethod

from .events import Events
from ..entities.entity import Entity


class Observer(ABC):
    @abstractmethod
    def on_notify(self, entity: Entity, event: Events):
        pass
