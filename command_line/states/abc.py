from abc import ABC, abstractmethod


class StateABC(ABC):
    def __init__(self, args: list):
        self._args = args

    @abstractmethod
    def get_state(self) -> dict: pass
