import unittest
from command_line.states import CommandWithParamsState


class TestCommandWithParamsState(unittest.TestCase):

    def test_state_name(self):
        args = ['add', 'param']
        state = CommandWithParamsState(args=args).get_state()
        self.assertEqual(state['state'], 'command with params')

    def test_state_args(self):
        args = ['add', 'param']
        state = CommandWithParamsState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')

    def test_state_difficult_args(self):
        args = ['add', '"param_123_1"']
        state = CommandWithParamsState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param_123_1')
