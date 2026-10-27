from .command import Command


class Commandhandler:
    def __init__(self) -> None:
        self.commands: list = []

    def add_command(self, command: Command) -> None:
        self.commands.append(command)

    def execute_commands(self) -> None:
        for command in self.commands:
            command.execute()
