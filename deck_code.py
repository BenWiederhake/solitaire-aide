#!/usr/bin/env python3

import common
import os
import sys


def run_encode(base):
    x = 0
    for i in range(base)
        b = sys.stdin.buffer.read(1)
        if b == b'':
            break


def run_decode(base):
    raise NotImplementedError()


def usage(progname):
    print('USAGE: {} {{encode | decode}} [<BASENUM>]'.format(progname), file=sys.stderr)
    exit(1)


def run(argv):
    if not 2 <= len(argv) <= 3:
        print('error: bad argument count', file=sys.stderr)
        usage(argv[0])

    base = None
    try:
        base = int(argv[2])
        if not 1 < base < 1000:
            print('error: "{}" is not a valid base (must be integer between 1 and 1000)'.format(argv[2]), file=sys.stderr)
            usage(argv[0])
    except IndexError:
        pass
    except ValueError:
        print('error: "{}" is not a valid base (must be integer)'.format(argv[2]), file=sys.stderr)
        usage(argv[0])
    if len(argv) == 2:
        base = os.environ.get('DECKCODE_BASE')
    if base is None:
        base = os.environ.get('DECKCODE_BASE')
    if base is None:
        base = 54
    else:
        print('note: base set to {}'.format(base), file=sys.stderr)

    if argv[1] == 'encode':
        run_encode(base)
    elif argv[1] == 'decode':
        run_decode(base)
    else:
        print('error: unknown command "{}"'.format(argv[1]), file=sys.stderr)
        usage(argv[0])


if __name__ == '__main__':
    run(sys.argv)
