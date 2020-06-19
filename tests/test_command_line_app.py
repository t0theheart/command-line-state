import unittest
from command_line import CommandLine
from command_line.exception import CommandLineException


class TestCommandLine(unittest.TestCase):

    def test_empty(self):
        program = CommandLine()
        program.parse_command_line('')
        state = program.get_state()
        self.assertEqual(state['state'], 'empty state')

    def test_command(self):
        program = CommandLine()
        program.parse_command_line('add')
        state = program.get_state()
        self.assertEqual(state['state'], 'command')
        self.assertEqual(state['command'], 'add')

    def test_command_with_error(self):
        program = CommandLine()
        try:
            program.parse_command_line('add123')
        except CommandLineException as e:
            self.assertEqual(str(e), 'command line is not valid.')

    def test_command_with_params(self):
        program = CommandLine()
        program.parse_command_line('add param')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')

    def test_command_with_difficult_params(self):
        program = CommandLine()
        program.parse_command_line('add "param_param_123_1"')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param_param_123_1')

    def test_command_with_params_and_key_without_params(self):
        program = CommandLine()
        program.parse_command_line('add param -c')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-c')

    def test_command_with_params_and_key_without_params_with_params(self):
        program = CommandLine()
        program.parse_command_line('add param -c key_param')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-c')

    def test_command_with_params_and_key_optional_params_without_params(self):
        program = CommandLine()
        program.parse_command_line('add param -n')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-n')

    def test_command_with_params_and_key_optional_params_with_params(self):
        program = CommandLine()
        program.parse_command_line('add param -n key_param')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-n')
        self.assertEqual(state['key_params'], 'key_param')

    def test_command_with_params_and_key_with_params(self):
        program = CommandLine()
        program.parse_command_line('add param -a key_param')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-a')
        self.assertEqual(state['key_params'], 'key_param')

    def test_command_with_params_and_key_with_difficult_params(self):
        program = CommandLine()
        program.parse_command_line('add param -a "key_param_123_1"')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-a')
        self.assertEqual(state['key_params'], 'key_param_123_1')

    def test_command_with_params_and_key_with_params_with_error(self):
        program = CommandLine()
        try:
            program.parse_command_line('add param -a')
        except CommandLineException as e:
            self.assertEqual(str(e), 'command line is not valid.')

    def test_command_with_difficult_params_and_key_with_difficult_params(self):
        program = CommandLine()
        program.parse_command_line('add "param_123_1" -a "key_param_123_1"')
        state = program.get_state()
        self.assertEqual(state['state'], 'command with params and key with params')
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param_123_1')
        self.assertEqual(state['key'], '-a')
        self.assertEqual(state['key_params'], 'key_param_123_1')
