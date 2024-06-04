# solitaire-aide

> Helps you learn the "solitaire" encryption.

This is a small set of tools I wrote to teach myself the
["solitaire" encryption](https://www.schneier.com/academic/solitaire/).

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [How to learn](#how-to-learn)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [Contribute](#contribute)

## Setup

Nothing is really needed.

By default, the algorithm determines the order as "Club-Diamonds-Hearts-Spade",
but you can set it to whatever.  Just set the environment variable `SOLITAIRE_ORDER`
to the initials of your desired order. Support for the
[French and German](https://en.wikipedia.org/wiki/Playing_card#Modern_deck_formats)
decks is built-in:

```
$ ./deck_read.py
Using SuitOrder CDHS ['Clubs', 'Diamonds', 'Hearts', 'Spades']
...
$ SOLITAIRE_ORDER="SEHL" ./deck_read.py
Using SuitOrder SEHL ['Schellen', 'Eichel', 'Herz', 'Laub']
...
$ SOLITAIRE_ORDER="ABCD" ./deck_read.py
Using SuitOrder ABCD ['A', 'B', 'C', 'D']
...
```

## Usage

The tools are listed in the order I wrote them.
I suggest to use them is this order.

### Converting cards in your head (`deck_read.py`)

This helps you with reading cards quickly and correctly.

You shuffle a deck of cards, and type the order as numbers into the program.
Afterwards, it tell you where you went wrong.

For example:

```
$ ./deck_read.py
SuitOrder CDHS ['Clubs', 'Diamonds', 'Hearts', 'Spades']
Enter 52-54 numbers between 1 and 54 as you read them from the deck.
Press Enter again to indicate the end of the deck.
> 20
> 1
> 7
(etc.)
> 36
> 17
> 12
>
[20, 1, 7, 34, 38, 40, 33, 25, 49, 10, 30, 8, 3, 35, 46, 18, 21, 31, 52, 28, 26, 47, 37, 39, 14, 51, 50, 11, 41, 45, 13, 42, 5, 37, 27, 19, 48, 44, 6, 2, 35, 15, 29, 43, 4, 23, 16, 9, 52, 36, 17, 12]
9 of Diamonds: Expected 1, got 0 instead.
J of Diamonds: Expected 1, got 0 instead.
6 of Hearts: Expected 1, got 0 instead.
9 of Hearts: Expected 1, got 2 instead.
J of Hearts: Expected 1, got 2 instead.
K of Spades: Expected 1, got 2 instead.
```

```
$ ./deck_read.py
SuitOrder CDHS ['Clubs', 'Diamonds', 'Hearts', 'Spades']
Enter 52-54 numbers between 1 and 54 as you read them from the deck.
Press Enter again to indicate the end of the deck.
> 14
> 32
(etc.)
> 20
> 10
>
[14, 32, 11, 38, 3, 18, 51, 40, 37, 43, 19, 15, 27, 2, 21, 13, 23, 30, 31, 46, 45, 52, 50, 26, 28, 36, 5, 34, 47, 41, 6, 1, 16, 33, 8, 48, 17, 49, 22, 44, 7, 42, 4, 12, 35, 9, 25, 24, 29, 39, 20, 10]
No issues.  Perfect!
```

### Letter-number-conversion (`stream_letters.py`)

This tool helps you learn to convert between letters and numbers and back.
You can try using `stream_calc.py` right away, and fall back to this if you
find yourself counting for most of the time,
because there's an easier way than just count.

### Modulo addition/subtraction (`stream_calc.py`)

This tool helps you in memorizing which letter with what key and which mode
(encrypting/decrypting) yields which letter.
It essentially gives you a letter-key pair and asks you for the result.
Repeat ad nauseum.

### Keystream Generation (`deck_operate.py`)

This little helper spews the keystream in a way that is reasonably-easy to analyze.
It is not really meant to be used, except as an `import` or to generate `sheet.tex` and `sheet.pdf`.

### Deck keying (`deck_key.py`)

FIXME

### Trying out example texts (`example_decode.py`, `example_encode.py`)

FIXME

## How to learn

Here's how I went about learning it.  Dunno if this helps you.

Play with `deck_read.py`.  Personally, I first query for the "suit offset",
and then add the card number to it (unless it's a king, then I just query
the next suit's offset; sometimes I do the same for queens; Jokars are easy).
So for 7 of Hearts I think "2 6 … 3 3", and of 9 of Spades I think "3 9 … 4 8".
The important part is to actually think (and not just type) the result,
because the result will eventually be needed for further operations (like count cut, etc.)
Shuffle decks and repeat until you get it right at least two decks in a row.

`stream_letters.py` taught me the skill of
converting numbers and letters: By coincidence, the German name of the letter `j` is `JOT`,
and the letters `JOT` just happen to be coincidentally the 10th, 15th, and 20th letter of the alphabet.
I already know the first few and last few letters by heart, so that allows for rapid conversion.

Next, I played with `stream_calc.py`, which puts this skill to the extremes: encode/decode random letters and offsets.
To make it a bit more realistic, and potentially train my brain to be faster around the most frequent letters,
I did not pick the *uniform* random letter distribution, but rather the actual frequencies of each letter in English text.

FIXME

## TODOs

* Implement `deck_key.py`
* Sample texts that feel nice
* Implement `example_{en,de}code.py`

## NOTDOs

* Efficient encryption/decryption
* Deck-input?

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/solitaire_aide/issues/new) or submit PRs.
