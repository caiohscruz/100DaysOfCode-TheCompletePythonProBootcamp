import random
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

blank = '_'
display = []
for _ in range(word_length):
  display.append(blank)

previous_guesses = []  

print(logo)

while not end_of_game:
   
  guess = input("Guess a letter: ").lower()

  clear()

  if guess in previous_guesses:
    print(f"You have already gessed letter '{guess}'")
  else:
    previous_guesses.append(guess)
    previous_guesses.sort()
    if guess in chosen_word:
      letters_count = 0
      for index, letter in enumerate(chosen_word):
        if letter == guess:
          display[index] = guess
          letters_count += 1
      if letters_count > 1:
        print(f"There're {letters_count} letters '{guess}' in this word")
      else:
        print(f"There's {letters_count} letter '{guess}' in this word")  
    else:
      lives -= 1  
      print(f"There isn't a letter '{guess}' in this word, you lose a life")
      if lives == 0:
        end_of_game = True
        print(f"You lose. The word was '{chosen_word}'")
   
  print(f"{' '.join(display)}")
  print(f"Previous guesses {'-'.join(previous_guesses)}")

  if not blank in display:
    end_of_game = True
    print("You win.")

  print(stages[lives])