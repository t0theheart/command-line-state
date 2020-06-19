import unittest
from command_line.states import EmptyState


class TestEmptyState(unittest.TestCase):

    def test_state_name(self):
        state = EmptyState(args=[]).get_state()
        self.assertEqual(state['state'], 'empty state')
