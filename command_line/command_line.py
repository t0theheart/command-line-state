from .abc import CommandLineABC
from .exception import command_line_is_not_valid
from .states import (
    StateABC,
    EmptyState,
    CommandState,
    CommandWithParamsState,
    CommandWithParamsAndKeyState,
    CommandWithParamsAndKeyWithParamsState
)
import re


command_keys_with_params = ['-a', '-r', '-p']
command_keys_optional_params = ['-n', '-m', '-l', '-s']
command_keys_without_params = ['-c']


class CommandLine(CommandLineABC):
    def __init__(self):
        self._state: StateABC = EmptyState(args=[])
        self._command_args: list = []

    def parse_command_line(self, command_line: str):
        if command_line:
            self._command_args = command_line.split()
            self._validate_first_arg()

            if len(self._command_args) >= 2:
                second_arg = self._command_args[1]
                if second_arg.startswith('"') or second_arg.startswith('\''):
                    self._command_args[1] = second_arg[1:-1]

                if len(self._command_args) >= 3:
                    third_arg = self._command_args[2]
                    if third_arg in command_keys_without_params:
                        self._state = CommandWithParamsAndKeyState(args=self._command_args)
                    elif third_arg in command_keys_optional_params:
                        if len(self._command_args) == 4:
                            self._state = CommandWithParamsAndKeyWithParamsState(args=self._command_args)
                        else:
                            self._state = CommandWithParamsAndKeyState(args=self._command_args)
                    elif third_arg in command_keys_with_params:
                        if len(self._command_args) == 4:
                            self._state = CommandWithParamsAndKeyWithParamsState(args=self._command_args)
                        else:
                            raise command_line_is_not_valid
                else:
                    self._state = CommandWithParamsState(args=self._command_args)
            else:
                self._state = CommandState(args=self._command_args)
        else:
            self._state = EmptyState(args=[])

    def _validate_first_arg(self):
        command = self._command_args[0]
        if not re.search('^[A-Za-z]*$', command):
            raise command_line_is_not_valid

    def get_state(self):
        return self._state.get_state()
