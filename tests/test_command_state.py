import unittest
from command_line.states import CommandState


class TestCommandState(unittest.TestCase):

    def test_state_name(self):
        args = ['add']
        state = CommandState(args=args).get_state()
        self.assertEqual(state['state'], 'command')

    def test_state_args(self):
        args = ['add']
        state = CommandState(args=args).get_state()
        self.assertEqual(state['command'], 'add')
