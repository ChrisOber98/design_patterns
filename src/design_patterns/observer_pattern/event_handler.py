import pygame
from pygame import Event

from .commands.command import Command
from .player import Player
from .commands.game_commands.set_player_direction import SetPlayerDirection


class EventHandler:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

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
            return SetPlayerDirection(self.player, -1)
        if event.key == pygame.K_d:
            return SetPlayerDirection(self.player, 1)

    def _process_keyup_event(self, event: Event) -> None:
        keys = pygame.key.get_pressed()

        if event.key == pygame.K_a:
            if keys[pygame.K_d]:
                return SetPlayerDirection(self.player, 1)
            else:
                return SetPlayerDirection(self.player, 0)
        if event.key == pygame.K_d:
            if keys[pygame.K_a]:
                return SetPlayerDirection(self.player, -1)
            else:
                return SetPlayerDirection(self.player, 0)
