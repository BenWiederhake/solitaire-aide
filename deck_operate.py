#!/usr/bin/env python3

# 1-indexed.
JOKER_A_CARD = 53;
JOKER_B_CARD = 54;


class Deck:
    def __init__(self, j_move_top='skip'):
        assert j_move_top in ['skip', 'slot', 'swap']
        self.cards = list(range(1, 54 + 1))
        self.j_move_top = j_move_top

    def move_single(self, j_pos):
        if j_pos < 53:
            self.cards[j_pos], self.cards[j_pos + 1] = self.cards[j_pos + 1], self.cards[j_pos]
        elif self.j_move_top == 'skip':
            # The solitaire move.  Not reversible.
            self.cards = [self.cards[0]] + [self.cards[-1]] + self.cards[1:-1]
        elif self.j_move_top == 'swap':
            # Reversible.
            self.cards[-1], self.cards[0] = self.cards[0], self.cards[-1]
        elif self.j_move_top == 'slot':
            # Reversible.  May lead to weird results.
            self.cards = self.cards[-1:] + self.cards[:-1]

    def move_jokers(self):
        self.move_single(self.cards.index(JOKER_A_CARD))
        self.move_single(self.cards.index(JOKER_B_CARD))
        self.move_single(self.cards.index(JOKER_B_CARD))

    def triple_cut(self):
        # Always reversible.
        a_pos = self.cards.index(JOKER_A_CARD)
        b_pos = self.cards.index(JOKER_B_CARD)
        if a_pos > b_pos:
            a_pos, b_pos = b_pos, a_pos
        self.cards = self.cards[b_pos + 1:] + self.cards[a_pos:b_pos + 1] + self.cards[:a_pos]

    def count_cut(self):
        # Always reversible.
        count = self.cards[-1]
        if count >= JOKER_A_CARD:
            # Nothing happens anyway.
            return
        self.cards = self.cards[count:-1] + self.cards[0:count] + [self.cards[-1]]

    def advance(self):
        self.move_jokers()
        #print('After moving:', self.cards)
        self.triple_cut()
        self.count_cut()

    def peek(self):
        offset = min(53, self.cards[0])
        return self.cards[(offset + 1) - 1]

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return repr(self.cards)


def run():
    deck = Deck(j_move_top='swap')
    for i in range(99999):
        #print('State: {}'.format(deck))
        deck.advance()
        print('Output: {}'.format(deck.peek()))
    print('Final state: {}'.format(deck))


if __name__ == '__main__':
    run()
