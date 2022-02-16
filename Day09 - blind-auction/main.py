from art import logo
from replit import clear

should_continue = 'yes'

auction_bids = {}

def find_winner(bids):
  winner_bid = 0
  for key, value in bids:
    if value > winner_bid:
      winner_name = key
      winner_bid = value
  print(f"The winner is {winner_name} with a bid of ${winner_bid}")


while should_continue == 'yes':
  print(logo)

  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))

  auction_bids[name] = bid

  should_continue = input("Are any other bidders? Type 'yes or 'no'\n")
  clear()

