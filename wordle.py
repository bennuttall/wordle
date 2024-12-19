from itertools import chain
from collections import Counter
from pathlib import Path
import sys
from datetime import datetime, date


EPOCH = date(2021, 6, 19)

today = datetime.now().date()
today_wordle_num = (today - EPOCH).days + 1


WORDLIST_FILE = Path('words.txt')
SOLUTIONS_LIST_FILE = Path('solutions.txt')

WORDS_LIST = [
    word.lower().strip()
    for word in WORDLIST_FILE.read_text().split()
]
WORDS = set(WORDS_LIST)
if len(WORDS) != len(WORDS_LIST):
    print("Word list contains duplicates")

SOLUTIONS_LIST = [
    word.lower().strip()
    for word in SOLUTIONS_LIST_FILE.read_text().split()
]
SOLUTIONS = set(SOLUTIONS_LIST)
if len(SOLUTIONS) != len(SOLUTIONS_LIST):
    "Solutions list contains duplicates"

def add_solution(word):
    if len(word) != 5:
        print("Word must be 5 characters")
    elif word not in WORDS:
        print("Word must be in wordlist")
    elif word in SOLUTIONS:
        print("Word already in solutions")
    else:
        with SOLUTIONS_LIST_FILE.open("a") as f:
            f.write(f"\n{word.upper()}")
        print(f"{word.upper()} added")
        SOLUTIONS.add(word)

def do_missing_solutions():
    missing_solutions = today_wordle_num - len(SOLUTIONS)

    if len(SOLUTIONS) > today_wordle_num:
        print("Too many words in solutions list")
    elif missing_solutions == 1:
        print("Missing today's solution")
    elif missing_solutions > 1:
        print(f"Missing {missing_solutions} solutions")
    else:
        print("Solutions list up to date")

def get_letter_counts(words):
    c = Counter(chain.from_iterable(words))
    return {letter: count for letter, count in c.most_common()}

def score_word(word, letter_counts):
    return sum([letter_counts[letter] for letter in set(word)])

BLACK_LETTERS = 'oed'
LETTER_1_GREEN = ''
LETTER_2_GREEN = ''
LETTER_3_GREEN = 'r'
LETTER_4_GREEN = ''
LETTER_5_GREEN = ''
LETTER_1_YELLOWS = 'a'
LETTER_2_YELLOWS = 'ra'
LETTER_3_YELLOWS = ''
LETTER_4_YELLOWS = 'st'
LETTER_5_YELLOWS = 's'
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

print(f"{len(WORDS) - len(SOLUTIONS):,} / {len(WORDS):,} remaining solutions")
if len(sys.argv) == 2:
    word = sys.argv[1].lower()
    add_solution(word)
    do_missing_solutions()
else:
    do_missing_solutions()

    letter_counts = get_letter_counts(possible_words)
    for word in sorted(possible_words, key=lambda w: score_word(w, letter_counts)):
        star = '*' if word in SOLUTIONS else ''
        print(f"{word.upper()} {score_word(word, letter_counts):,} {star}")
    print(f"{len(possible_words):,} possible words")


# letters = set('cxgmvkw')

# def foo(w):
#     return sum(c in w for c in letters)

# words = {
#     word
#     for word in WORDS
#     if any(c in letters for c in word)
# }

# pw = [w for w in words if foo(w) == 3]
# for w in pw:
#     print(w)