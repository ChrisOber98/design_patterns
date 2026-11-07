import pygame

from ..command import Command


class QuitGame(Command):
    def execute(self) -> None:
        pygame.quit()
        raise SystemExit
