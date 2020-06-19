from .abc import StateABC


class CommandWithParamsAndKeyState(StateABC):
    def get_state(self) -> dict:
        return {
            'state': 'command with params and key',
            'command': self._args[0],
            'command_params': self._args[1],
            'key': self._args[2]
        }
