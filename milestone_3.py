def check_guess(guess, secret_word):
    """Check if the guessed letter is in the secret word."""
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(secret_word):
    """Ask the user for a letter and validate it."""
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, secret_word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Sample secret word
secret_word = "apple"  # In a real scenario, this could be randomly selected

# Call the function to start the guessing process
ask_for_input(secret_word)