from art import logo 
from dicts import deck
from replit import clear
import random

def begin_game():
  clear()
  print(logo)

def deal_card(hand):
  hand.append(random.choice(list(deck)))
  return hand

def deal_hand():
  hand = []
  for _ in range(2):
    hand = deal_card(hand)
  return hand

def deal_dealer_hand():
  hand = deal_hand()
  print(f'Computer first card: [{hand[0]}]')
  return hand

def deal_player_hand():
  hand = deal_hand()
  print(f'Your cards: {draw_cards(hand)}\n')
  return hand

def draw_cards(hand):
  drawing = ''
  for card in hand:
    drawing += f"[{card}]"
  return drawing

def pick_card(player_hand):
  player_hand = deal_card(player_hand)
  print(f'Your hand: {draw_cards(player_hand)}\n')
  player_score = compute_score(player_hand)
  if player_score < 22:
    burst = False
  else:
    burst = True
    print('Burst!')
  return {
    'hand': player_hand,
    'burst': burst
  }

def compute_score(hand):
  values = []
  for card in hand:
    values.append(deck[card])
  points = sum(values)
  if (points > 21 and 11 in values):
    num_Aces = values.count(11)
    while (points > 21 and num_Aces > 0):
      num_Aces -=1
      points -= 10
  elif (points == 21 and len(values) == 2):
      points = 0
  return points

def compute_dealer_score(dealer_hand):
  dealer_points = compute_score(dealer_hand)
  while (dealer_points < 12 and dealer_points != 0):
    print(f"\nComputer hand: {draw_cards(dealer_hand)}")
    print("Computer has less than 12 points")
    print("Computer picks one card")
    dealer_cards = deal_card(dealer_hand)
    dealer_points = compute_score(dealer_hand)
  return dealer_points

def end_game(dealer_hand, player_hand): 
  dealer_points = compute_dealer_score(dealer_hand)
  player_points = compute_score(player_hand)
  print(f'\nComputer final hand: {draw_cards(dealer_hand)}')
  print(f'Your final hand: {draw_cards(player_hand)}\n')
  if (player_points > 21): 
    result = 'You lose.'
  elif (player_points == dealer_points):
    result = 'Draw.'
  elif (player_points == 0):
    result = 'Blackjack! You win.'
  elif (dealer_points == 0):
    result = 'Blackjack! You lose.'
  elif (player_points > dealer_points):
    result = 'You win.'
  else:
    result = 'You lose.'
  print(result)