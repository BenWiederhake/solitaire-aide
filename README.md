# solitaire-aide

> Helps you learn the "solitaire" encryption.

This is a small set of tools I wrote to teach myself the
["solitaire" encryption](https://www.schneier.com/academic/solitaire/).

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [Contribute](#contribute)

## Setup

Nothing is really needed.

By default, the algorithm determines the order as "Club-Diamonds-Hearts-Spade",
but you can set it to whatever.  Just set the environment variable `SOLITAIRE_ORDER`
to the initials of your desired order. For example:

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

### `deck_read.py`

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
> 38
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

## TODOs

* Everything
* Sample texts that feel nice?

## NOTDOs

* Efficient encryption/decryption

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/solitaire_aide/issues/new) or submit PRs.
