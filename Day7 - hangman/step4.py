#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
blank = '_'

display = []
for _ in range(word_length):
  display.append(blank)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  if guess in chosen_word:
    for index, letter in enumerate(chosen_word):
      if letter == guess:
        display[index] = guess
  else:
    print('Miss')
    lives -= 1  

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if lives == 0:
      end_of_game = True
      print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if not blank in display:
    end_of_game = True
    print("You win.")

  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

  print(f"{stages[lives]} {display}")