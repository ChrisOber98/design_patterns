import pygame
from pygame import Event

from .commands.command import Command
from .commands.game_commands.set_entity_x_velocity import SetEntityXVelocity
from .commands.game_commands.set_entity_y_velocity import SetEntityYVelocity
from .entities.entity import Entity


class EventHandler:
    def __init__(self, player: Entity) -> None:
        self.player: Entity = player

    def process_input(self) -> Command | None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._process_quit_event()
            elif event.type == pygame.KEYDOWN:
                return self._process_keydown_event(event)
            elif event.type == pygame.KEYUP:
                return self._process_keyup_event(event)

    def _process_quit_event(event: Event) -> None:
        pygame.quit()
        raise SystemExit

    def _process_keydown_event(self, event: Event) -> Command:
        if event.key == pygame.K_a:
            return SetEntityXVelocity(self.player, -5)
        if event.key == pygame.K_d:
            return SetEntityXVelocity(self.player, 5)
        if event.key == pygame.K_SPACE and self.player.y_velocity == 0:
            return SetEntityYVelocity(self.player, 20)

    def _process_keyup_event(self, event: Event) -> None:
        keys = pygame.key.get_pressed()

        if event.key == pygame.K_a:
            if keys[pygame.K_d]:
                return SetEntityXVelocity(self.player, 5)
            else:
                return SetEntityXVelocity(self.player, 0)
        if event.key == pygame.K_d:
            if keys[pygame.K_a]:
                return SetEntityXVelocity(self.player, -5)
            else:
                return SetEntityXVelocity(self.player, 0)
