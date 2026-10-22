import pygame

from game_commands import (
    MoveDownCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveUpCommand,
)


class EventHandler:
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    return MoveUpCommand
                if event.key == pygame.K_a:
                    return MoveLeftCommand
                if event.key == pygame.K_s:
                    return MoveDownCommand
                if event.key == pygame.K_d:
                    return MoveRightCommand
