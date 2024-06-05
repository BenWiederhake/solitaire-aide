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

### Entropy Computation (`basic_entropy.py`)

This little helper simply computes the generated entropy in a passphrase when picking a sequence of uniformly random words from the list in `wordlist_basic_english_prefixfree.json` until a certain given minimum length is reached. The Basic English wordlist has a length of 850, making it prefixfree shortens it to 800.

A few key results:

```
minlength= 4 results in an entropy of 10.644406269463854 bits.
minlength= 5 results in an entropy of 13.429310840666052 bits.
minlength= 6 results in an entropy of 15.68103071277608 bits.
minlength= 7 results in an entropy of 17.24949964784788 bits.
minlength= 8 results in an entropy of 18.774294873311764 bits.
minlength= 9 results in an entropy of 20.640026565002984 bits.
minlength=10 results in an entropy of 22.633576795740655 bits.
minlength=15 results in an entropy of 31.612087425558588 bits.
minlength=20 results in an entropy of 40.63462859886208 bits.
minlength=25 results in an entropy of 49.674164299222824 bits.
minlength=30 results in an entropy of 58.716557210651104 bits.
minlength=35 results in an entropy of 67.75915640290033 bits.
minlength=40 results in an entropy of 76.8017094146745 bits.
minlength=45 results in an entropy of 85.8442417662776 bits.
minlength=50 results in an entropy of 94.88677009489663 bits.
```

Anything above 50 characters is unlikely to increase real security, and 25
characters seems to be a secure-enough trade-off for most usecases. Anything
below 10 characters can easily be enumerated. 15 characters seems to be a good
point where the desire for ease of use and the desire for security are both
left unfulfilled to equal extents.

### Deck keying (`deck_key.py`)

Creates a key passphrase, and a ciphertext, along with some "human debug info". With this you can try out the full decoding experience. Example:

```
$ ./deck_key.py
Key: DRESSTIREDBEAUTIFUL
# Base64 of cleartext: TUFMRVdBUlJJQ0VXT1VORFpaWlo=
# Keyed deck: [15, 16, 10, 38, 39, 51, 52, 25, 54, 21, 48, 17, 37, 1, 2, 7, 19, 26, 27, 6, 30, 8, 20, 35, 22, 11, 32, 50, 46, 53, 9, 33, 34, 18, 40, 41, 5, 49, 43, 42, 44, 47, 28, 29, 3, 4, 31, 23, 24, 36, 12, 13, 14, 45]
# Key stream: [8, 52, 46, 51, 22, 1, 5, 31, 18, 16, 16, 22, 15, 54, 7, 20, 20, 14, 38, 48, 21]
Ciphertext: UAFDS BWWAS USDBH XNLVU
# This will take about 33:13 minutes.
```

I'm still quite untrained, and that time estimate is based on my personal
decoding speed. Note that even this very short passphrase and ciphertext
already take half an hour to decode!

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

Then, try out `sheet.pdf`. This means you start with a fully sorted deck; I
find that perfectly sorting a deck is very quick, so starting from scratch is
relatively cheap. Then, simply start generating the keystream. The joker cards
are are written in italics, because the jokers won't appear in the actual
keystream used for the encryption, but do appear in physical terms. I strongly
recommend learning the "slot" variant, see [below](#slot-versus-skip).

Note that this is the most frustrating and time-consuming part: It takes 15-20
minutes per line, the first three lines exercise basically all edge cases that
exist, and being a chaotic encryption process, it is absolutely unforgiving
regarding errors. I highly recommend filming yourself, and reviewing the
footage whenever you find that there was an error, because it is
nigh-impossible to determine the source of the error after the fact otherwise.
Here are some sources of error that I tend to make, and their mitigations.
Feel free to copy my approach; but I'm sure there's better approaches:

- Mixing up phases: The count cut and the "Find the output card"-step feel nearly identical, so sometimes when I'm done counting and have determined the card, I don't remember which of the two steps I was in. Now I keep the bottommost card between my left pinky and ringfinger while counting during the count cut, and leave these fingers empty during the "output card" step.
- Miscounting: Sometimes cards are stickier than they look, sometimes they slip past my fingers, sometimes I actually forget how to count. Mitigation: Count everything twice, ideally in independent ways. Mark the card after the first way, and only accept if the second way matches. Restart from scratch if there is any error. This is actually quite complex, and I cound in different ways:
    - 1-13 (Ace of Clubs through King of Clubs): Just straight-up count the same cards twice.
    - 14-25 (Ace of Diamonds through Queen of Diamonds): In the first way, first count the number (i.e. 1 to 12), then the suit (i.e. always 13). In the second way, the other way around.
    - 26-39 (King of Diamonds through King of Hearts): Count 13 forwards twice, then count the number, mark, count the rest towards 13, then count 13 again. Exactly two cards should remain. This ends up being two independent measurements.
    - 40-52 (Ace of Spades through Kinf of Spades): Count backwards, i.e. hold the bottom two cards away (possibly including the count cut card, if doing the count cut step), think "13", and count down from there. Mark the card, count up again. Two cards should be remaining (again).
    - 53-54 (Jokers): No-op.
    - This is the slowest step by far. I might experiment with counting only once, if my error rate becomes low enough, in order to speed up by factor two.
- Mixing up Hearts and Diamonds: This is so silly, I don't know why this keeps happening. Mitigation: Think the name of the suit as a word explicitly.

Each line in `sheet.pdf` is 15 cycles, and results in an expected 14.44…
keystream numbers (14.3 in this case). You should be able to get the first two
lines right most of the time, and reach the *fifth* line at least once before
moving on. Try out `stream_calc.py` from time to time, so that this skill
doesn't atrophy.

Finally, `deck_key.py` brings it all together: Given a passphrase and a
ciphertext, decode that ciphertext. This is pretty much the real-life usecase!
If it becomes too easy for you, or you are actually much faster than I am, I
recommend cranking up the `KEY_LENGTH_MIN` to 15-20, and `TEXT_LENGTH_MIN`
arbitrarily high (note that you can easily stop before being "done", and still
be able to learn from it.) Like in the previous step, I recommend filming
yourself while doing it, so that you can easily go back in time and review and
learn from your errors.

At this point, congratulations, you're a fully-fledged Solitaire-decoder! You're now on every watchlist of every secret police. You're welcome.

## Slot versus skip

Bruce Schneier's definition of Solitaire says about moving the Joker card down:

> If the joker is the bottom card of the deck, move it just below the top card.

This is not reversible, and widely regarded a mistake. I call this the `'skip' variant`.

I'm going to instead take the following model: The deck of cards is a ring
with no defined beginning or end, and instead there is a special 55th card
"Hand". So in the initial sorted order, there is (somewhere) the sequence "…,
QueenSpades, KingSpades, JokerA, JokerB, Hand, AceClubs, TwoClubs, …". In this
model, moving a Joker a card down becomes trivial to define: Simply swap it
with the next "card". In the example, moving Joker B would result in the
sequence "…, QueenSpades, KingSpades, JokerA, Hand, JokerB, AceClubs,
TwoClubs, …". Note that in physical reality this means putting the Joker card
on top of the deck. I named this variant `'slot' variant`, because it treats
the "hand" as a slot like any other slot. The generated keystream is
incompatible with the 'skip' variant. I perceive this as the easiest fix,
although I have not actually calculated the actual impact of this change, or
even whether this "improvement" actually is an improvement.

Note that [Analysis of Solitaire arXiv:1909.06300](https://arxiv.org/abs/1909.06300)
computes that Solitaire leaks information at a rate of 0.0005 bits per
character produced after the first, and suggests various ways to counteract
this bias. However, these are too labor-intensive.

## TODOs

* Sample texts that feel nice?
* Implement `example_{en,de}code.py`
* Read the calculation in https://arxiv.org/abs/1909.06300 again, try to find other modifications that reduce the repetition-bias with less work.

## NOTDOs

* Efficient encryption/decryption
* Deck-input

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/solitaire_aide/issues/new) or submit PRs.
