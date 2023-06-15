#Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
print('''   _   _   _   _   _   _     _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ 
 ( N | u | m | b | e | r ) ( G | u | e | s | s | i | n | g )
  \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ ''')
print("\n")
print("Welcome to the Number Guessing name!")
print("I'm thinking of a number between 1 and 100!")
difficulty = input("Choose a difficulty. Type 'easy' or hard: ")
# Allow the player to submit a guess for a number between 1 and 100.
computer_number = random.randint(1, 100)
attempts = 0
game = True

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while game:
    print(f"You have {attempts} attempts to guess the number.")

    user_guess = int(input("Make a guess: "))
    
    if user_guess != computer_number:
        attempts -= 1
        if user_guess < computer_number:
            print("Too low")
        else:
            print("Too high")

        if attempts == 0:
            game = False
            print("You've run out of guesses. You lose!")
            break
            
        print("Guess again")
    else:
        game = False
        print(f"You got it! The answer was {computer_number}.")


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

