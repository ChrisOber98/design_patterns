from command import Command


class MoveUpCommand(Command):
    def execute(self, player, command_list):
        player.y = player.y - 300
        if player.y < 0:
            player.y = 0
            return False
        return True

    def undo(self, player, command_list):
        player.y = player.y + 300


class MoveDownCommand(Command):
    def execute(self, player, command_list):
        player.y += 300
        if player.y > 600:
            player.y = 600
            return False
        return True

    def undo(self, player, command_list):
        player.y = player.y - 300


class MoveLeftCommand(Command):
    def execute(self, player, command_list):
        player.x -= 300
        if player.x < 0:
            player.x = 0
            return False
        return True

    def undo(self, player, command_list):
        player.x = player.x + 300


class MoveRightCommand(Command):
    def execute(self, player, command_list):
        player.x += 300
        if player.x > 600:
            player.x = 600
            return False
        return True

    def undo(self, player, command_list):
        player.x = player.x - 300


class UndoMoveCommand(Command):
    def execute(self, player, command_list):
        if len(command_list) == 0:
            return False

        for command in command_list:
            print(command)

        current_command = command_list[-1]

        if current_command:
            current_command.undo(player, command_list)
            command_list.pop()

        return False
