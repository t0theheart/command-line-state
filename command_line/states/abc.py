from abc import ABC, abstractmethod


class StateABC(ABC):
    def __init__(self, args: list):
        self._args = args

    @staticmethod
    def _stringify_difficult_param(string: str):
        if string.startswith('"') and string.endswith('"') or string.startswith('\'') and string.endswith('\''):
            string = string[1:-1]
        return string

    @abstractmethod
    def get_state(self) -> dict: pass
