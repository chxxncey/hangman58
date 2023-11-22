import random

class WordGame:
    
    def __init__(self, word_list, max_misses=5):
        self.secret_word = self.get_random_word(word_list)
        self.missed_letters = []  
        self.remaining_misses = max_misses
        self.display_word = self.get_display_word()
        
    def get_random_word(self, word_list):
        return random.choice(word_list)
    
    def get_display_word(self):
        return ["_"] * len(self.secret_word)
        
    def receive_guess(self):
        while True:
            guess = input("Guess a letter: ")
            if self.validate_guess(guess):
                return guess
                
    def validate_guess(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single letter.") 
            return False
        elif letter in self.missed_letters or letter in self.display_word:
            print("You already guessed that letter.")
            return False
        else:
            return True
            
    def update_display_word(self, letter):        
        for i, secret_letter in enumerate(self.secret_word):
            if secret_letter == letter:
                self.display_word[i] = letter  
                
    def apply_guess(self, letter):
        if letter in self.secret_word:
            self.update_display_word(letter)
        else:
            self.remaining_misses -= 1
            self.missed_letters.append(letter)
            
    def check_win(self):
        if "_" not in self.display_word: 
            print("You win!")
            return True
    
    def check_loss(self):                                   
        if self.remaining_misses == 0:
            print("You lost!") 
            return True
        
word_list = ["apple", "banana", "cherry"]
game = WordGame(word_list)
game.apply_guess("a") 
print(game.display_word)