#!/usr/bin/env python3

import collections
import deck_key
import math


def compute_entropy(distrib, minlength, cache):
    assert minlength >= 1
    if minlength not in cache:
        assert 0 not in distrib
        num_entries = sum(distrib.values())
        entropy = 0.0
        for consumed_length, num_options in distrib.items():
            if consumed_length >= minlength:
                subentropy = 0.0
            else:
                subentropy = compute_entropy(distrib, minlength - consumed_length, cache)
            prob_branch = num_options / num_entries
            branch_entropy = math.log2(num_entries)
            entropy += prob_branch * (subentropy + branch_entropy)
        cache[minlength] = entropy
    return cache[minlength]


def run():
    words = deck_key.load_dictionary()
    lengths = collections.Counter(len(w) for w in words)
    distrib = {k: v for k, v in lengths.items()}
    cache = dict()
    for minlength in range(1, 50 + 1):
        e = compute_entropy(distrib, minlength, cache)
        print(f"minlength={minlength:2} results in an entropy of {e} bits.")
    print(f"For reference: KEY_LENGTH_MIN={deck_key.KEY_LENGTH_MIN}, TEXT_LENGTH_MIN={deck_key.TEXT_LENGTH_MIN}")


if __name__ == "__main__":
    run()
