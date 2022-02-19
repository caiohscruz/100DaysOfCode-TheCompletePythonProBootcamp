import random
from art import logo
from replit import clear

EASY_NUM_ATTEMPTS = 10
HARD_NUM_ATTEMPTS = 5

DIFFICULTY_OPTIONS = {
    'easy' : EASY_NUM_ATTEMPTS,
    'hard': HARD_NUM_ATTEMPTS
  }

MIN_NUMBER = 1
MAX_NUMBER = 100

def setup_game():
  print(logo) 
  print("Welcome to the Number Guessing Game!")

def set_number():
  print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}")
  return random.randint(MIN_NUMBER, MAX_NUMBER) 

def get_attempts():
  choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  while choosen_difficulty not in DIFFICULTY_OPTIONS:
    print("Option incorrect")
    choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  return DIFFICULTY_OPTIONS[choosen_difficulty]


def play_game():
  setup_game()
  number = set_number()
  attempts = get_attempts() 
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