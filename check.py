from itertools import chain
from collections import Counter
from pathlib import Path


WORDLIST = Path('words.txt')
SOLUTIONS_LIST = Path('solutions.txt')

WORDS = {
    word.lower().strip()
    for word in WORDLIST.read_text().split()
}

SOLUTIONS = {
    word.lower().strip()
    for word in SOLUTIONS_LIST.read_text().split()
}

def get_letter_counts(words):
    c = Counter(chain.from_iterable(words))
    mc = c.most_common()
    return {letter: count for letter, count in mc}

def score_word(word, letter_counts):
    return sum([letter_counts[letter] for letter in set(word)])

BLACK_LETTERS = ''
LETTER_1_GREEN = ''
LETTER_2_GREEN = ''
LETTER_3_GREEN = ''
LETTER_4_GREEN = ''
LETTER_5_GREEN = ''
LETTER_1_YELLOWS = ''
LETTER_2_YELLOWS = ''
LETTER_3_YELLOWS = ''
LETTER_4_YELLOWS = ''
LETTER_5_YELLOWS = ''
YELLOWS = LETTER_1_YELLOWS + LETTER_2_YELLOWS + LETTER_3_YELLOWS + LETTER_4_YELLOWS + LETTER_5_YELLOWS

possible_words = {
    word
    for word in WORDS
    if all(c not in word for c in BLACK_LETTERS)
    and all(c in word for c in YELLOWS)
    and (word[0] == LETTER_1_GREEN if LETTER_1_GREEN else True)
    and (word[1] == LETTER_2_GREEN if LETTER_2_GREEN else True)
    and (word[2] == LETTER_3_GREEN if LETTER_3_GREEN else True)
    and (word[3] == LETTER_4_GREEN if LETTER_4_GREEN else True)
    and (word[4] == LETTER_5_GREEN if LETTER_5_GREEN else True)
    and word[0] not in LETTER_1_YELLOWS
    and word[1] not in LETTER_2_YELLOWS
    and word[2] not in LETTER_3_YELLOWS
    and word[3] not in LETTER_4_YELLOWS
    and word[4] not in LETTER_5_YELLOWS
}

letter_counts = get_letter_counts(possible_words)
for word in sorted(possible_words, key=lambda w: score_word(w, letter_counts)):
    star = '*' if word in SOLUTIONS else ''
    print(f"{word.upper()} {score_word(word, letter_counts):,} {star}")
print(f"{len(possible_words):,} possible words")

# letters = ''

# def foo(w):
#     return sum(c in w for c in letters)

# words = {
#     word
#     for word in WORDS
#     if any(c in letters for c in word)
# }

# pw = sorted(words, key=lambda w: foo(w), reverse=True)
# for w in pw[:10]:
#     print(w)