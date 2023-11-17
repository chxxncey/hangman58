# Step 1: Ask the user to enter a single letter
print("Please enter a single letter:")
guess = input()  # Assign the input to a variable called guess

# Step 1: Check if the length of the input is 1 and if the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement
    print("Good guess!")
else:
    # Step 3: Create an else block for invalid input
    print("Oops! That is not a valid input.")

# Step 1: Create a list of 5 favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Orange", "Grapes"]

# Step 2: Assign this list to a variable called word_list
word_list = favorite_fruits

# Step 3: Print out the newly created list
print(word_list)

# Step 4: Import random module
import random

# Step 4 and 5: Create the random.choice method and assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Step 6: Print out word
print(word)

