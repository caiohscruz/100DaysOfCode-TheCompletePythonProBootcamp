from art import logo
from replit import clear

should_continue = 'yes'

auction_bids = {}

winner_bid = 0

while should_continue == 'yes':
  print(logo)

  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))

  auction_bids[name] = bid

  if bid > winner_bid:
    winner_name = name
    winner_bid = bid

  should_continue = input("Are any other bidders? Type 'yes or 'no'\n")
  clear()

print(f"The winner is {winner_name} with a bid of ${winner_bid}")