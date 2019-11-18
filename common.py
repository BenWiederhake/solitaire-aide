import enum
import os


DEFAULT_ORDER = 'CDHS'

SUITS_FRENCH = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades'}
SUITS_GERMAN = {'E': 'Eichel', 'S': 'Schellen', 'H': 'Herz', 'L': 'Laub'}


class SuitOrder:
    def __init__(self, order=DEFAULT_ORDER, name_hint=None):
        self.order = list(order)  # Copy
        assert len(self.order) == len(set(self.order))
        self.names = [name_hint.get(e, e) if name_hint else e for e in self.order]

    def resolve_char2index(self, char):
        return self.order.index(char)

    def resolve_index2char(self, index):
        return self.order[index]

    def resolve_index2name(self, index):
        return self.names[index]

    def __str__(self):
        return 'SuitOrder {} {}'.format(
            ''.join(self.order),
            self.names,
        )


class CardNames:
    def __init__(self, suit_order):
        self.suit_order = suit_order

    def name_within(self, card_index):
        if card_index <= 10:
            return str(card_index)
        #return 'UOK'[card_index - 11]  # Too much effort to distinguish this properly
        return 'JQK'[card_index - 11]

    def name(self, total_index, distinguish_jokers=True):
        suit_i, card_i = divmod(total_index - 1, 13)
        if suit_i == 4:
            if distinguish_jokers:
                return ['Joker A', 'Joker B'][card_i]
            else:
                return 'Joker'
        return '{} of {}'.format(
            self.name_within(card_i + 1),
            self.suit_order.resolve_index2name(suit_i))


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
