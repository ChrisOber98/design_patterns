from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, player, command_list):
        pass
