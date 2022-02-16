#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
blank = '_'

display = []
for _ in range(word_length):
  display.append(blank)

previous_guesses = []  

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in previous_guesses:
      print(f"You have already gessed letter {guess}")
    else:
      previous_guesses.append(guess)
      #Check guessed letter
      if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
          if letter == guess:
            display[index] = guess
      #Check if user is wrong.
      else:
        lives -= 1  
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"There isn't a letter '{guess}' in this word, you lose a life")
        if lives == 0:
          end_of_game = True
          print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if not blank in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])