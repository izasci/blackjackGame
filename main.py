
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from art import logo
from replit import clear

def finding_card(hand):
  return hand.append(random.choice(cards))

def summarize(hand):
  hand_sum = 0
  for card in hand:
    hand_sum += card
  if hand_sum > 21:
    if 11 in hand:
      hand.remove(11)
      hand.append(1)
      hand_sum = 0
      for card in hand:
        hand_sum += card
  return int(hand_sum)

def print_final(player_hand, computer_hand, result_player, result_computer):
  print(f"  Your final hand:{player_hand}, final score: {result_player}\n  Computer's final hand: {computer_hand}, final score: {result_computer}")

def end_game(player_hand, computer_hand, result_player, result_computer, known_card):
  play_again = True 
  while play_again == True:
    if result_computer == 21 and len(computer_hand) == 2:
        print_final(player_hand, computer_hand, result_player, result_computer)
        print("Opponent has BlackJack. You lose.")
        play_again = False
    elif result_player == 21 and len(computer_hand) == 2:
      print_final(player_hand, computer_hand, result_player, result_computer)
      print("BlackJack. You win.")
      play_again = False
    elif result_player > 21:
        print_final(player_hand, computer_hand, result_player, result_computer)
        print("You went over. You lose.")
        play_again = False
    elif result_player < 21:
      draw = input("Type 'y' to get another card, type 'n' to pass ")
      if draw not in ["y", "n"]:
        end_game(player_hand, computer_hand, result_player, result_computer, known_card)
      elif draw == "y":
        finding_card(player_hand)
        result_player = summarize(player_hand)
        print(f"  Your cards: {player_hand}, current score: {result_player}")
        print(f"  Computer's first card: {known_card}")
        result_computer = computer_draw(computer_hand, result_computer)
      else:
        play_again = False
        while result_computer <= 16:
          result_computer = computer_draw(computer_hand, result_computer)
          result_computer = summarize(computer_hand)
        print_final(player_hand, computer_hand, result_player, result_computer)
        if result_player <= 21:
          if result_computer > 21:
            print("Opponent went over. You win")
          elif result_player > result_computer:
            print("You are closer to 21. You win")
          elif result_player == result_computer:
            print("Draw")
          else:
              print("Opponent is closer to 21. You lose.")
        elif result_player > 21:
          print_final(player_hand, computer_hand, result_player, result_computer)
          print("You went over. You lose.")

          
def computer_draw(computer_hand, result_computer):
  if result_computer <= 16:
    finding_card(computer_hand)
    result_computer = summarize(computer_hand)
  return summarize(computer_hand)  

def game():
  print(logo)
  player_hand = []
  computer_hand = []
  finding_card(player_hand)
  finding_card(player_hand)
  sum = summarize(player_hand)
  print(f"  Your cards: {player_hand}, current score: {sum}")
  finding_card(computer_hand)
  finding_card(computer_hand)
  comp_sum = summarize(computer_hand)
  if computer_hand[0] == 11:
    known_card = computer_hand[1]
  else:
    known_card = computer_hand[0]
  print(f"  Computer's first card: {known_card}")
  end_game(player_hand, computer_hand, sum, comp_sum, known_card)

blackjack = True
while blackjack == True:
  play = input("Do you want to play in BlackJack? y or n ").lower()
  if play == "y":
    clear()
    game()
  elif play == "n":
    blackjack = False
    clear()
    print(logo)
    print("Goodbye")
