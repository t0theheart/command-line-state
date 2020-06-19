from .abc import StateABC


class EmptyState(StateABC):
    def get_state(self) -> dict:
        return {
            'state': 'empty state'
        }
