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


def compute_single(mode_mult, letter, key):
    letter_val = ord(letter) - ord('A')
    out_val = (letter_val + mode_mult * key + 26) % 26
    out_letter = chr(out_val + ord('A'))
    return out_letter


def print_hint(mode_mult):
    print('    ' + ENGLISH_LETTERS)
    print()
    for key in range(1, 26 + 1):
        print('{:2}  {}'.format(key, ''.join(compute_single(mode_mult, letter, key) for letter in ENGLISH_LETTERS)))
    print()


def run_single(mode_mult, letter, key):
    expected_letter = compute_single(mode_mult, letter, key)
    try:
        while True:
            line = input('{}, {} ?> '.format(letter, key))
            line = line.upper().strip()
            if line == 'HINT':
                print_hint(mode_mult)
                continue
            if not line:
                continue
            if len(line) != 1:
                print('It needs to be a single letter, like "W", "t", or "F" (case does not matter).')
                continue
            actual_letter = line
            if expected_letter == actual_letter:
                return True
            print('\nNope, it should be "{}".  Try again:'.format(expected_letter))
            # Force the user to try again the same combination.
    except KeyboardInterrupt:
        print('\nInterrupted.')
        return False
    except EOFError:
        print()  # Line break
        return False


def run_random(mode_mult, freqs):
    key = random.randrange(1, 26 + 1)
    letter = random.choices(*freqs)[0]
    if mode_mult == +1:
        pass
    elif mode_mult == -1:
        # If we're decoding, the *output* distribution
        # needs to match the requested distribution.
        encoded_letter = compute_single(+1, letter, key)
        assert letter == compute_single(mode_mult, encoded_letter, key), (encoded_letter, letter, key)
        letter = encoded_letter
    else:
        raise AssertionError(mode_mult)
    return run_single(mode_mult, letter, key)


def run_with(is_encoding, freqs, introduce):
    mode_mult = [-1, +1][is_encoding]
    if introduce:
        mode_str = ['DECRYPTION', 'ENCRYPTION'][is_encoding]
        mode_op = ['SUBTRACT', 'ADD'][is_encoding]
        print('Running in {} mode, so you need to {} the keystream.'.
            format(mode_str, mode_op))
        print('Format of the queries is "LETTER, KEY ?> ", and you enter the resulting LETTER.')
        print('You can also type "hint" to have the {} table displayed.'.format(mode_str))
        print('You can also type "rot13" to have the ROT13 table displayed.')
        print()
    # Make sure the first is easy:
    answered = run_single(mode_mult, 'A', 1)
    while answered:
        answered = run_random(mode_mult, freqs)


def build_parser(progname=None):
    parser = argparse.ArgumentParser(
        prog=progname,
        description="Trains your ability to calculate letters using modulo.")
    freq = parser.add_mutually_exclusive_group()
    freq.add_argument("--uniform", action='store_true', help='Set all frequencies to be equal.')
    freq.add_argument('--freq-string', help='String of length at least 1, and indicates how often each letter may appear, but repeating them respectively more or less often.  For example, "AAAB" only tests letters A and B; and letter A three times as often as letter B.')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--encode", action='store_true', help='Train encoding.')
    mode.add_argument('--decode', action='store_true', help='Train decoding.')
    return parser


def determine_encoding(args):
    if args.encode:
        return True, False
    if args.decode:
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
    is_encoding, introduce = determine_encoding(args)
    freqs = determine_freqs(parser, args)

    run_with(is_encoding, freqs, introduce)


if __name__ == '__main__':
    run(sys.argv)
