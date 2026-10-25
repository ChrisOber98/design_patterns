from pathlib import Path
from random import randint, choice

import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SHIP_PATH = Path(__file__).parent / "ship.bmp"


class ProjectileImage:
    def __init__(self):
        self.SHIP = pygame.image.load(SHIP_PATH).convert()


class Projectile:
    def __init__(self, screen, image):
        self.screen = screen

        self.x, self.y = self.get_random_position()
        self.x_direction = choice([-1, 1])
        self.y_direction = choice([-1, 1])
        self.speed = 5
        self.image = image

    def get_random_position(self):
        return (randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))

    def check_for_edge_hit(self):
        counter = 0

        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.y_direction *= -1
            self.y = max(0, min(self.y, SCREEN_HEIGHT))
            counter += 1

        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.x_direction *= -1
            self.x = max(0, min(self.x, SCREEN_WIDTH))
            counter += 1

        return counter

    def update(self):
        self.x += self.x_direction * self.speed
        self.y += self.y_direction * self.speed

    def draw(self):
        self.screen.blit(self.image.SHIP, (self.x, self.y))


def run():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    image = ProjectileImage()

    clock = pygame.time.Clock()

    projectiles = [Projectile(screen, image)]

    font = pygame.font.SysFont(None, 30)
    info_text = font.render("", True, (255, 255, 255))
    frame_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        screen.fill("purple")

        counter = 0

        for projectile in projectiles.copy():
            counter += projectile.check_for_edge_hit()
            projectile.update()
            projectile.draw()

        if counter:
            for i in range(counter):
                projectiles.append(Projectile(screen, image))

        counter = 0

        frame_count += 1
        if frame_count % 30 == 0:
            info_text = font.render(
                f"FPS: {clock.get_fps():.0f}   Projectiles: {len(projectiles)}",
                True,
                (0, 0, 0),
            )

        screen.blit(info_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
