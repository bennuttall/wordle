from string import ascii_lowercase
import random


with open('/usr/share/dict/american-english') as f:
    ALL_WORDS = {
        word.strip()
        for word in f
        if all(c in ascii_lowercase for c in word.strip())
    }


class Wordle:
    def __init__(self, word=None, *, size=5):
        if word is None:
            self.make_word_list(size)
            word = self.random_word()
        else:
            self.make_word_list(len(word))
        self.word = word
        self.guesses = []

    def random_word(self):
        return random.choice(list(self.WORDS))

    def make_word_list(self, size):
        words = {word for word in ALL_WORDS if len(word) == size}
        plurals = {
            word
            for word in words
            if word.endswith('s')
            and word[:4] in ALL_WORDS
        }
        self.WORDS = words - plurals

    def guess(self, word):
        assert len(word) == len(self.word)
        assert word in self.WORDS
        unknowns = {
            letter
            for pos, letter in enumerate(word)
            if letter != self.word[pos]
        }
        result = tuple(
            (letter, self.letter_score(pos, letter, unknowns))
            for pos, letter in enumerate(word)
        )
        self.guesses.append(result)
        return result

    def letter_score(self, pos, letter, unknowns):
        if letter == self.word[pos]:
            return 2
        if letter in self.word and letter in unknowns:
            return 1
        return 0