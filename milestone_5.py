import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guessed letter is in the word and update word_guessed or decrement num_lives."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    if self.word_guessed[i] == '_':  # Only reduce num_letters for first occurrence
                        self.num_letters -= 1
                    self.word_guessed[i] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Ask the user for a letter and validate it."""
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    """Function to play the Hangman game."""
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print("Current word guessed:", ''.join(game.word_guessed))
        else:
            print("Congratulations. You won the game!")
            break

# Example word list
word_list = ["apple", "banana", "cherry"]

# Call the function to play the game
play_game(word_list)
