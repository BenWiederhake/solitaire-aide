#!/usr/bin/env python3

import argparse
import random
import sys


ENGLISH_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_FREQUENCIES = [
    0.08167, 0.01492, 0.02202, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
    0.06966, 0.00153, 0.01292, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929,
    0.00095, 0.05987, 0.06327, 0.09356, 0.02758, 0.00978, 0.02560, 0.00150,
    0.01994, 0.00077,
]


def print_hint():
    for letter in ENGLISH_LETTERS:
        number = ord(letter) - ord('A') + 1
        print('{:2}: {}'.format(number, letter))
    print()


def run_single(is_lettring, letter):
    number = ord(letter) - ord('A') + 1
    try:
        while True:
            prompt = number if is_lettring else letter
            line = input('{:2}>? '.format(prompt))
            line = line.upper().strip()
            if line == 'HINT':
                print_hint()
                continue
            if not line:
                continue
            if is_lettring:
                if len(line) != 1:
                    print('It needs to be a single letter, like "W", "t", or "F" (case does not matter).')
                    continue
                actual = line
                expected = letter
            else:
                expected = number
                try:
                    actual = int(line)
                    assert 1 <= actual <= 26
                except (ValueError, AssertionError):
                    print('It needs to be a single number between 1 and 26, like 13.')
                    continue
            if expected == actual:
                return True
            print('\nNope, it should be "{}".  Try again:'.format(expected))
            # Force the user to try again the same query.
    except KeyboardInterrupt:
        print('\nInterrupted.')
        return False
    except EOFError:
        print()  # Line break
        return False


def run_random(is_lettring, freqs):
    letter = random.choices(*freqs)[0]
    return run_single(is_lettring, letter)


def run_with(is_lettring, freqs, introduce):
    if introduce:
        mode_str = ['to-number', 'to-letter'][is_lettring]
        print('Running in {} mode.'. format(mode_str))
        print('You can also type "hint" to have the table displayed.')
        print()
    # Make sure the first is easy:
    answered = run_single(is_lettring, 'A')
    while answered:
        answered = run_random(is_lettring, freqs)


def build_parser(progname=None):
    parser = argparse.ArgumentParser(
        prog=progname,
        description="Trains your ability to calculate letters using modulo.")
    freq = parser.add_mutually_exclusive_group()
    freq.add_argument("--uniform", action='store_true', help='Set all frequencies to be equal.')
    freq.add_argument('--freq-string', help='String of length at least 1, and indicates how often each letter may appear, but repeating them respectively more or less often.  For example, "AAAB" only tests letters A and B; and letter A three times as often as letter B.')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--to-letter", action='store_true', help='Train conversion to letters.')
    mode.add_argument('--to-number', action='store_true', help='Train conversion to numbers.')
    return parser


def determine_lettring(args):
    if args.to_letter:
        return True, False
    if args.to_number:
        return False, False
    # Random.  Since this is the default, also introduce the query format.
    return random.getrandbits(1), True


def determine_freqs(parser, args):
    if args.uniform:
        return (ENGLISH_LETTERS, None)
    if args.freq_string is not None:
        if len(args.freq_string) < 1:
            print('error: "--freq-string" needs a string of length at least 1',
                file=sys.stderr)
            parser.usage()
        freq_string = args.freq_string.strip().upper()
        if not all(c in ENGLISH_LETTERS for c in freq_stringfreq_string):
            print('error: "--freq-string" should consist only of uppercase english letters',
                file=sys.stderr)
            parser.usage()
        return (freq_string, None)
    return (ENGLISH_LETTERS, ENGLISH_FREQUENCIES)


def run(argv):
    parser = build_parser(argv[0])
    args = parser.parse_args(argv[1:])
    is_lettring, introduce = determine_lettring(args)
    freqs = determine_freqs(parser, args)

    run_with(is_lettring, freqs, introduce)


if __name__ == '__main__':
    run(sys.argv)
