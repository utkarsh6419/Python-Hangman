"""A compact terminal hangman game."""

import random

WORDS = ("python", "banana", "planet", "garden", "window")


def main():
    word = random.choice(WORDS)
    guessed = set()
    misses = 0
    while misses < 6 and not set(word).issubset(guessed):
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\n{display}   misses: {misses}/6")
        letter = input("Guess one letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha() or letter in guessed:
            print("Enter one new letter.")
            continue
        guessed.add(letter)
        if letter not in word:
            misses += 1
    print(f"You {'won' if misses < 6 else 'lost'}! The word was '{word}'.")


if __name__ == "__main__":
    main()
