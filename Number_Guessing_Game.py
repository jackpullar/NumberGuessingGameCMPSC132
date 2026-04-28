import random

class Number_Guessing: 

    def __init__ (self, level): #initializes a new game and all attributes, creates new target number

        self.target = random.randint(1, 100)
        self.guesses = []
        self.tries = 0
        self.active_game = True
        self.winner = False

    def get_input(self): #takes in the user input, ensuring it is valid

        while True:
            try:
                guess = int(input("Enter an integer between 1 and 100: "))
                if guess in self.guesses:
                    print(f"You already guessed {guess}! Try a new number.") #doesn't allow the user to reguess a number
                elif 1 <= guess <= 100:
                    return guess
                else:
                    print("Enter an integer between 1 and 100.")
            except ValueError: #handles errors
                print("That's not a valid integer. Please enter a valid integer between 1 and 100.")