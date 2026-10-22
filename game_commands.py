from command import Command


class MoveUpCommand(Command):
    def execute(self, player):
        player.y = player.y - 300
        if player.y < 0:
            player.y = 0


class MoveDownCommand(Command):
    def execute(self, player):
        player.y += 300
        if player.y > 600:
            player.y = 600


class MoveLeftCommand(Command):
    def execute(self, player):
        player.x -= 300
        if player.x < 0:
            player.x = 0


class MoveRightCommand(Command):
    def execute(self, player):
        player.x += 300
        if player.x > 600:
            player.x = 600
