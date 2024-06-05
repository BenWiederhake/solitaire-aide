#!/usr/bin/env python3

import base64
import deck_operate
import json
import random
import stream_calc

# Must be any of {'skip', 'slot', 'swap'}.
DEFAULT_J_MOVE_TOP = "slot"
DICTIONARY = "wordlist_basic_english_prefixfree.json"
KEY_LENGTH_MIN = 15
TEXT_LENGTH_MIN = 15

# These are roughly my times, still quite untrained, in seconds per letter.
# The TIME_PER_TEXT could be significantly decreased if I could avoid double-checking, but then the error rate would explode.
TIME_PER_KEY = 21.5
TIME_PER_TEXT = 79.2


def load_dictionary():
    with open(DICTIONARY, "r") as fp:
        return json.load(fp)


def create_phrase_min_length(dictionary, min_length):
    phrase = ""
    while len(phrase) < min_length:
        phrase += random.choice(dictionary)
    return phrase


def group_five(letters):
    akku = []
    for i, letter in enumerate(letters):
        if i != 0 and i % 5 == 0:
            akku.append(" ")
        akku.append(letter)
    return "".join(akku)


def run():
    dictionary = load_dictionary()
    key = create_phrase_min_length(dictionary, KEY_LENGTH_MIN)
    print(f"Key: {key}")
    cleartext = create_phrase_min_length(dictionary, TEXT_LENGTH_MIN)
    while len(cleartext) % 5 != 0:
        cleartext += "Z"
    b64cleartext = base64.b64encode(cleartext.encode()).decode()
    print(f"# Base64 of cleartext: {b64cleartext}")
    deck = deck_operate.Deck(j_move_top=DEFAULT_J_MOVE_TOP)
    for key_letter in key:
        assert "A" <= key_letter <= "Z"
        given_count = ord(key_letter) - ord("A") + 1
        deck.advance(given_count=given_count)
    print(f"# Keyed deck: {deck}")
    ciphertext = []
    key_stream = []
    text_index = 0
    while text_index < len(cleartext):
        deck.advance()
        key_number = deck.peek()
        key_stream.append(key_number)
        if key_number >= deck_operate.JOKER_A_CARD:
            # Cannot encode!
            continue
        cipher_letter = stream_calc.compute_single(+1, cleartext[text_index], key_number)
        ciphertext.append(cipher_letter)
        text_index += 1
    print(f"# Key stream: {key_stream}")
    print(f"Ciphertext: {group_five(ciphertext)}")
    expected_time = TIME_PER_KEY * len(key) + TIME_PER_TEXT * len(cleartext)
    expected_minutes = int(expected_time / 60)
    expected_seconds = int(expected_time % 60 + 0.5)
    print(f"# This will take about {expected_minutes:02}:{expected_seconds:02} minutes.")


if __name__ == "__main__":
    run()
