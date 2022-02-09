alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, cipher_direction):
  new_text = ""

  if cipher_direction == "encode":
    shift = shift_amount
  elif cipher_direction == "decode":
    shift = -shift_amount

  for char in input_text:
    if char in alphabet:
      index = alphabet.index(char) + shift
      normal_index = index % len(alphabet)
      new_text += alphabet[normal_index]
    else:
      new_text +=  char  
    
  print(f"The {cipher_direction}d text is: {new_text}\n")

from art import logo
print(logo)

should_continue = 'yes'

while (should_continue == 'yes'):

  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

  should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Good bye!")