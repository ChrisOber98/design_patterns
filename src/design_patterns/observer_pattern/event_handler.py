import pygame


class EventHandler:
    def __init__(self):
        pass

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
