import random

def hangman():
    """
    Plays a text-based Hangman game.
    """

    words = ["python", "java", "javascript", "c++", "ruby", "php", "swift", "kotlin", "go", "rust"]
    word = random.choice(words)
    hidden_word = ["_" for _ in word]
    guesses_left = 6

    print("Welcome to Hangman!")
    print("You have 6 guesses to guess the word.")

    while guesses_left > 0 and "_" in hidden_word:
        print("".join(hidden_word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in word:
            for i, letter in enumerate(word):
                if guess == letter:
                    hidden_word[i] = guess
            print("Good guess!")
        else:
            guesses_left -= 1
            print(f"Wrong guess. {guesses_left} guesses remaining.")

    if "_" not in hidden_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"You ran out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()