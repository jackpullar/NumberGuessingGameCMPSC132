import random

class Number_Guessing: 

    def __init__ (self, level): #initializes a new game and all attributes, creates new target number

        self.target = random.randint(1, 100)
        self.guesses = []
        self.tries = 0
        self.active_game = True
        self.winner = False

        self.max_tries = self.DIFFICULTIES[level] #determines max number of guesses

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

    def check_guess(self,guess): #checks if the user guessed correctly and provides feedback

        if guess == self.target:
            self.active_game = False
            self.winner = True
            print(f"\nCorrect! Congrats! It took you {self.tries} tries!") #woohoo, winner!
        elif guess > self.target:
            print("\nToo high. Guess a lower number!")
        else:
            print("\nToo low. Guess a higher number!")
        
        if (self.tries == self.max_tries) and self.active_game: #checks if the user has used all available guesses
            self.active_game = False
            print(f"\nGame Over! You have no more tries! The number was {self.target}.")
           
    
    def game(self): #runs the game and updates the amount of guesses

        while self.active_game:
            if len(self.guesses) != 0:
                print(f"\nPrevious guesses: {self.guesses}!") #shows what the user has previously guessed

            print(f"\nYou have {self.max_tries-self.tries} tries!\n")

            user_guess = self.get_input() #section runs all the other methods
            self.tries += 1
            self.guesses.append(user_guess)
            self.check_guess(user_guess)

    def get_difficulty(): #input to determine difficulty of game (number of guesses allowed)

        while True:
            try:
                level = input("Please enter difficulty (easy, medium, or hard): ") 
                level = level.lower().strip() #formats level to match dictionary
                
                if level in ["easy","medium","hard"]:
                        return level
                else:
                    print("Please input a valid difficulty: easy, medium, or hard.")

            except ValueError: #catches error
                print("Invalid input. Try again!")