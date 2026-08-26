import random

# 5 predefined words
words = ["python", "computer", "keyboard", "developer", "program"]

# Choose a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses allowed.")

while wrong_guesses < max_wrong_guesses:

    # Show the current word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the whole word has been guessed
    complete = True

    for letter in secret_word:
        if letter not in guessed_letters:
            complete = False

    if complete:
        print("\nCongratulations!")
        print("You guessed the word:", secret_word)
        break

    # Get a letter from the player
    guess = input("Enter one letter: ").lower().strip()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Good guess!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")

# Player lost
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")