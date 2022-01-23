import colorama
from colorama import Back, Style

from wordle import Wordle


colorama.init()

messages = {
    1: "1 / 6 - Genius!",
    2: "2 / 6 - Magnificent",
    3: "3 / 6 - Impressive",
    4: "4 / 6 - Splendid",
    5: "5 / 6 - Great",
    6: "6 / 6 - Phew",
}


def play():
    game = Wordle()
    for i in range(1, 7):
        while True:
            guess = input("Guess: ").lower()
            if len(guess) != len(game.word):
                print(f"Guess must be {len(game.word)} letters")
            elif guess not in game.WORDS:
                print("Not in word list")
            else:
                break
        result = game.guess(guess)
        for letter, letter_score in result:
            if letter_score == 2:
                print(Back.GREEN + letter.upper(), end='')
            elif letter_score == 1:
                print(Back.YELLOW + letter.upper(), end='')
            elif letter_score == 0:
                print(Back.BLACK + letter.upper(), end='')
        print(Style.RESET_ALL)
        if all(r[1] == 2 for r in result):
            print()
            print(messages[i])
            show_result(game)
            return
    print("X / 6", game.word.upper())
    show_result(game)


def show_result(game):
    print()
    for guess in game.guesses:
        for letter, letter_score in guess:
            if letter_score == 2:
                print("🟩", end=' ')
            elif letter_score == 1:
                print("🟨", end=' ')
            elif letter_score == 0:
                print("⬛", end=' ')
        print(end='\n\n')

if __name__ == '__main__':
    play()