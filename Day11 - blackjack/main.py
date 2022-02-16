############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from functions import begin_game, deal_dealer_hand, deal_player_hand, pick_card, end_game

continue_playing = True

while continue_playing == True:
  begin_game()
  dealer_hand = deal_dealer_hand()
  player_hand = deal_player_hand() 
  continue_asking = True 
  while continue_asking:
    if (input("Do you want pick one more card? Type 'y' or 'n': ") == 'y'):
      picking = pick_card(player_hand)
      player_hand = picking['hand']
      continue_asking = not picking['burst']
    else:
      break;
  end_game(dealer_hand, player_hand)
  if (input("\nDo you want play more? Type 'y' or 'n': ") != 'y'):
    continue_playing = False
