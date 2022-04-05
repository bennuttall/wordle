from string import ascii_lowercase
from itertools import chain
from collections import Counter

LINUX_SYSTEM_DICT = '/usr/share/dict/american-english'
MAC_SYSTEM_DICT = '/usr/share/dict/words'
BIG_WORDLIST = 'words.txt'

wordlist = LINUX_SYSTEM_DICT
# wordlist = MAC_SYSTEM_DICT
wordlist = BIG_WORDLIST


with open(wordlist) as f:
    ALL_WORDS = {
        word.lower().strip()
        for word in f
        if all(c.lower() in ascii_lowercase for c in word.strip())
    }

WORDS = {word for word in ALL_WORDS if len(word.strip()) == 5}

PLURALS = {word for word in WORDS if word.endswith('s') and word[:4] in ALL_WORDS}
UNIQUE_LETTER_WORDS = {word for word in WORDS if len(set(word)) == 5}
WORDS = WORDS - PLURALS

c = Counter(chain.from_iterable(WORDS))
mc = c.most_common()
letter_counts = {letter: count for letter, count in mc}

def score_word(word):
    return sum([letter_counts[letter] for letter in set(word)])

word_scores = {word: score_word(word) for word in WORDS}

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

for word in sorted(possible_words, key=lambda w: word_scores[w]):
    print(word, word_scores[word])
print(len(possible_words), "possible words")