# solitaire-aide

> Healps you learn the "solitaire" encryption.

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

## TODOs

* Everything
* Sample texts that feel nice?

## NOTDOs

* Efficient encryption/decryption

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/solitaire_aide/issues/new) or submit PRs.
