from ..entities.entity import Entity
from ..observer.events import Events
from ..observer.observer import Observer
from .text_box import TextBox


class Scoreboard(TextBox, Observer):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        color: tuple[int, int, int] = (0, 0, 0),
        text: str | None = None,
    ):
        TextBox.__init__(self, x=x, y=y, color=color, text=text)
        self.score: int = 0
        self.render_score()

    def render_score(self) -> None:
        self.render(f"Score: {self.score}")

    def on_notify(self, entity: Entity, event: Events):
        match event:
            case Events.EDGE_COLLISION:
                self.score += 1
                self.render_score()
            case Events.PLAYER_COLLISION:
                pass
