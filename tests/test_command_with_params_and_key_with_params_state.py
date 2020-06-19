import unittest
from command_line.states import CommandWithParamsAndKeyWithParamsState


class TestCommandWithParamsAndKeyWithParamsState(unittest.TestCase):

    def test_state_name(self):
        args = ['add', 'param', '-a', 'key_param']
        state = CommandWithParamsAndKeyWithParamsState(args=args).get_state()
        self.assertEqual(state['state'], 'command with params and key with params')

    def test_state_args(self):
        args = ['add', 'param', '-a', 'key_param']
        state = CommandWithParamsAndKeyWithParamsState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-a')
        self.assertEqual(state['key_params'], 'key_param')

    def test_state_difficult_args(self):
        args = ['add', 'param', '-a', '"key_param_123_1"']
        state = CommandWithParamsAndKeyWithParamsState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
        self.assertEqual(state['command_params'], 'param')
        self.assertEqual(state['key'], '-a')
        self.assertEqual(state['key_params'], 'key_param_123_1')
