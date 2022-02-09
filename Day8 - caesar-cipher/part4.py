alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, cipher_direction):
  new_text = ""

  if cipher_direction == "encode":
    shift = shift_amount
  elif cipher_direction == "decode":
    shift = -shift_amount

  for char in input_text:
    #TODO-2: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      index = alphabet.index(char) + shift
      normal_index = index % len(alphabet)
      new_text += alphabet[normal_index]
    else:
      new_text +=  char  
    
  print(f"The {cipher_direction}d text is: {new_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-3: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
execute = 'yes'

while (execute == 'yes'):

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

  execute = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")