import pygame


class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, 300, 300)

        self.x = 0
        self.y = 0

        self.width = 300
        self.height = 300

        self.color = (255, 255, 255)

    def update_pos(self, x=None, y=None):
        if x:
            self.rect = x

        if y:
            self.rect = y

    def draw(self):
        pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.height)
        )
