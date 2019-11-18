import enum
import os


DEFAULT_ORDER = 'CDHS'

SUITS_FRENCH = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades'}
SUITS_GERMAN = {'E': 'Eichel', 'S': 'Schellen', 'H': 'Herz', 'L': 'Laub'}


class SuitOrder:
    def __init__(self, order, name_hint=None):
        self.order = list(order)  # Copy
        assert len(self.order) == len(set(self.order))
        self.names = [name_hint.get(e, e) if name_hint else e for e in self.order]

    def resolve_char2index(self, char):
        return self.order.index(char)

    def resolve_index2char(self, index):
        return self.order[index]

    def resolve_index2name(self, index):
        return self.names[index]

    def resolve_char2name(self, char):
        return self.resolve_index2name(self.resolve_char2index(char))

    def __str__(self):
        return 'SuitOrder {} {}'.format(
            ''.join(self.order),
            self.names,
        )


def get_order():
    env_order = os.environ.get('SOLITAIRE_ORDER', DEFAULT_ORDER)
    if len(env_order) != 4 or len(set(env_order)) != 4:
        raise ValueError(
            'Expected a suit-order (4 unique characters, e.g.{}), got {} instead.'
            .format(DEFAULT_ORDER, env_order))
    hint = None
    if set(env_order) == SUITS_FRENCH.keys():
        hint = SUITS_FRENCH
    elif set(env_order) == SUITS_GERMAN.keys():
        hint = SUITS_GERMAN
    return SuitOrder(env_order, hint)
