import unittest
from command_line.states import CommandWithParamsAndKeyState


class TestCommandWithParamsAndKeyState(unittest.TestCase):

    def test_state_name(self):
        args = ['add', 'param', '-a']
        state = CommandWithParamsAndKeyState(args=args).get_state()
        self.assertEqual(state['state'], 'command with params and key')

    def test_state_args(self):
        args = ['add', 'param', '-a']
        state = CommandWithParamsAndKeyState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-a')
