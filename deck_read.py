#!/usr/bin/env python3

import common


def read_deck():
    deck = list()
    print('Enter 52-54 numbers between 1 and 54 as you read them from the deck.')
    print('Press Enter again to indicate the end of the deck.')
    try:
        while True:
            line = input('> ')
            if not line:
                break
            try:
                val = int(line)
            except ValueError:
                print('"{}" does not look like a number.  NOT ADDED!'.format(line))
                continue
            if 1 <= val <= 54:
                deck.append(val)
            else:
                print('{} is not between 1 and 54.  NOT ADDED!'.format(val))
                continue
    except KeyboardInterrupt:
        print('\nInterrupted.')
        exit(1)
    except EOFError:
        print()  # Line break
        pass  # This is fine.
    return deck


def analyze_deck(deck):
    counts = [None] + [0] * 54
    for e in deck:
        counts[e] += 1
    issues = []
    if not 52 <= len(deck) <= 54:
        issues.append({'which': 'total', 'actual': len(deck), 'expected': (52, 53, 54)})
    for i in range(1, 52 + 1):
        if counts[i] == 1:
            continue
        issues.append({'which': i, 'actual': counts[i], 'expected': (1,)})
    if counts[54]:
        if counts[54] != 1:
            issues.append({'which': 54, 'actual': counts[54], 'expected': (0, 1)})
        if counts[53] != 1:
            issues.append({'which': 53, 'actual': counts[53], 'expected': (1,)})
    else:
        if counts[53] != 0 and counts[53] != 2:
            issues.append({'which': 53, 'actual': counts[53],
                'expected': (0, 2), 'distinguish': False})
    return issues


def print_analysis(analysis, card_names):
    if not analysis:
        print('No issues.  Perfect!')
        return
    for issue in analysis:
        if issue['which'] == 'total':
            print('The overall amount is off.  Expected 52-54 cards, got {} instead.'.format(issue['actual']))
            continue
        print('{}: Expected {}, got {} instead.'.format(
            card_names.name(issue['which'], issue.get('distinguish', True)),
            ' or '.join(str(e) for e in issue['expected']),
            issue['actual'],
        ))


def run():
    order = common.get_order()
    print(order)
    deck = read_deck()
    print(deck)
    analysis = analyze_deck(deck)
    print_analysis(analysis, common.CardNames(order))


if __name__ == '__main__':
    run()
