from ..entities.entity import Entity
from .events import Events
from .observer import Observer


class Subject:
    def __init__(self):
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, entity: Entity, event: Events):
        for observer in self.observers:
            if observer == entity:
                observer.on_notify(entity, event)
