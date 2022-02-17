from art import logo

import random
from replit import clear

difficulty_options = {'easy' : 10, 'hard': 5}

def play_game():
  print(logo) 
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  number = random.randint(1,100)
  choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  while choosen_difficulty not in difficulty_options:
    print("Option incorrect")
    choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = difficulty_options[choosen_difficulty]
  is_game_over = False
  while (not is_game_over):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess != number:
      attempts -= 1
      if guess > number: 
        print("Too high")
      else:
        print("Too low")
      if attempts > 0:
        print("Guess again")
      else:
        print(f"You've run out of guesses, you lose. The answer was {number}.")
        is_game_over = True
    else:
      print(f"You got it! The answer was {number}.")
      is_game_over = True
    
should_continue = True
while should_continue:
  clear()
  play_game()
  if (input("Type 'y' to play again or anything else to exit: ") != 'y'):
    should_continue = False