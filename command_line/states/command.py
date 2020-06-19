from .abc import StateABC


class CommandState(StateABC):
    def get_state(self) -> dict:
        return {
            'state': 'command',
            'command': self._args[0]
        }
