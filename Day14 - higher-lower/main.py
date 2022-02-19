from art import logo, vs
from replit import clear
from game_data import data
import random

continue_playing = True

while continue_playing:
  score = 0
  is_game_over = False
  while not is_game_over:
    clear()
    print(logo)

    if (score == 0):
      first_option = random.choice(data) 
      second_option =  first_option       
    else:
      print(f"You're right! Current score: {score}")
      first_option = second_option
      
    while second_option == first_option:
      second_option = random.choice(data)
    
    has_more_followers = 'A' if first_option['follower_count'] > second_option['follower_count'] else 'B'

    print(f"Compare A: {first_option['name']}, a {first_option['description']}, from {first_option['country']}")
    print(vs)
    print(f"Against B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    if (guess == has_more_followers):
      score += 1
    else:
      is_game_over = True
    
  print(f"Sorry, that's wrong. Final score: {score}")
  
  if (input("Do you wanna play one more time? Type 'y' to yes or anything else to no") != 'y'):
    continue_playing = False
