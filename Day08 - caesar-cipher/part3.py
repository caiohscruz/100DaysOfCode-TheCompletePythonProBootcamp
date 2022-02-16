alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(input_text, shift_amount, cipher_direction):
  new_text = ""

  if cipher_direction == "encode":
    shift = shift_amount
  elif cipher_direction == "decode":
    shift = -shift_amount

  for letter in input_text:
    index = alphabet.index(letter) + shift
    normal_index = index % len(alphabet)
    new_letter = alphabet[normal_index]
    new_text += new_letter

  print(f"The {cipher_direction}d text is: {new_text}")
  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, cipher_direction=direction)