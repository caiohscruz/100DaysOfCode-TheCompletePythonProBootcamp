from art import logo
from replit import clear

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):  
  return a / b

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide, 
}


def calculator():
  print(logo)

  print("Operations avaiable:")
  for symbol in operations:
    print(symbol)

  f_number = int(input("What is the first number? "))

  should_continue = True

  while should_continue:

    symbol_operation = input("Pich an operation: ")

    s_number = int(input("What is the next number? "))

    calc_function = operations[symbol_operation]

    answer = calc_function(f_number,s_number)

    print(f"{f_number} {symbol_operation} {s_number} = {answer}")

    if (input("Type 'y' if do you want continue calculate with the {answer} or type anything else to start a new calculation: ") == 'y'):
      f_number = answer
    else:
      should_continue: False
      clear()
      calculator()

calculator()