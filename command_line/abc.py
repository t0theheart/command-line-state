from abc import ABC, abstractmethod


class CommandLineABC(ABC):
    @abstractmethod
    def parse_command_line(self, line: str): pass

    @abstractmethod
    def get_state(self): pass
