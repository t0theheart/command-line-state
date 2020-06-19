from .abc import StateABC


class CommandWithParamsState(StateABC):
    def get_state(self) -> dict:
        return {
            'state': 'command with params',
            'command': self._args[0],
            'command_params': self._args[1]
        }
