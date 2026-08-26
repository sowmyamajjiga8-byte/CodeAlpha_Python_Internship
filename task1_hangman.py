import random

WORDS = ["python", "coding", "computer", "program", "developer"]
MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("\n=== Hangman Game ===")
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print("Attempts left:", attempts_left)

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts_left -= 1
            print("Incorrect!")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
