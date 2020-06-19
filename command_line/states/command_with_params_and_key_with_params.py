from .abc import StateABC


class CommandWithParamsAndKeyWithParamsState(StateABC):
    def get_state(self) -> dict:
        return {
            'state': 'command with params and key with params',
            'command': self._args[0],
            'command_params': self._args[1],
            'key': self._args[2],
            'key_params': self._args[3]
        }
