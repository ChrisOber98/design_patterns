from ..entities.entity import Entity
from ..observer.events import Events
from ..observer.observer import Observer
from .text_box import TextBox


class InfoBox(TextBox, Observer):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        color: tuple[int, int, int] = (0, 0, 0),
        text: str | None = None,
    ):
        TextBox.__init__(self, x=x, y=y, color=color, text=text)
        text = "A: Moves Left\nD: Moves Right\nSpace: Jump\nQ: Quits game"
        self.render(text)

    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.EDGE_COLLISION:
                pass
            case Events.PLAYER_COLLISION:
                pass
