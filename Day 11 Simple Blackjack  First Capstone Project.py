# Day 11 - First Capstone Project - Simplified Blackjack

# Rules notes
# first card dealt to dealer and player is visible, 2nd card to dealer is not shown
# have to handle Aces - count as 11 until score > 21
# dealer must draw if total less than 17


# art assets
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

you_won = """
 /$$     /$$                        /$$      /$$                    
|  $$   /$$/                       | $$  /$ | $$                    
 \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$  /$$$$$$  /$$$$$$$ 
  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$ /$$__  $$| $$__  $$
   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$  \ $$| $$  \ $$
    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$  | $$
    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$  | $$
    |__/  \______/  \______/       |__/     \__/ \______/ |__/  |__/
"""    

you_lost = """
$$\     $$\                         $$\                            $$\     
\$$\   $$  |                        $$ |                           $$ |    
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |      $$$$$$\   $$$$$$$\ $$$$$$\   
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  _____|\_$$  _|  
   \$$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |\$$$$$$\    $$ |    
    $$ |  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\   $$ |$$\ 
    $$ |  \$$$$$$  |\$$$$$$  |      $$$$$$$$\\$$$$$$  |$$$$$$$  |  \$$$$  |
    \__|   \______/  \______/       \________|\______/ \_______/    \____/ 
"""

busted = """
 ____  _  _  ____  ____  ____  ____  _   
(  _ \/ )( \/ ___)(_  _)(  __)(    \/ \  
 ) _ () \/ (\___ \  )(   ) _)  ) D (\_/  
(____/\____/(____/ (__) (____)(____/(_) 
"""

was_draw = """
 _____     ______     ______     __     __    
/\  __-.  /\  == \   /\  __ \   /\ \  _ \ \   
\ \ \/\ \ \ \  __<   \ \  __ \  \ \ \/ ".\ \  
 \ \____-  \ \_\ \_\  \ \_\ \_\  \ \__/".~\_\ 
  \/____/   \/_/ /_/   \/_/\/_/   \/_/   \/_/ 
"""



import random
from IPython.display import clear_output

# deal a card randomly, each value has equal weight, we're not doing a fancy card + suit (for now)
def hit_me():
  card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  return card_list[random.randint(0, 12)]

# given a hand (list of cards), provide the score. Convert face cards to 10, handle aces based on the total score
def get_score(hand):   
  user_score = 0
  aces = 0

  for card in hand:
    if card in ('J', 'Q', 'K'):
      user_score  += 10
    elif card == 'A': # first pass through, count aces as 11
      user_score += 11
      aces += 1
    else:
      user_score += int(card)
  
  while user_score > 21 and aces > 0: # if the hand total is more than 21 and there's an ace, change it to count like a 1
    user_score -= 10
    aces -= 1

  return user_score    

# show both the player's hand and the first card of the dealer's hand, leave flag in show_cards to show all of the dealer's cards at the end
def show_hands(p_hand, d_hand, show_cards):
  user_score = get_score(p_hand)
  dealer_score = get_score(d_hand)
    
  print(f"Your cards: {p_hand}, current score: {user_score}")
  if show_cards == 0:
    print(f"Dealer's card(s): {d_hand[0]}")
  else:
    print(f"Dealer's card(s): {d_hand}, current_score: {dealer_score}")      


# initialize continue as true to guarantee first pass
continue_game = True


while continue_game == True:
  print(logo)
  print("Welcome to Blackjack!")
  # initialize values for first game, reset values for extra games
  player_hand = []
  dealer_hand = []
  player_choice = ''
  show_cards = 0
  player_bust = False
  player_wins = False
  player_draw = False  

  # this is the initial deal of 2 cards each
  player_hand.append(hit_me())
  player_hand.append(hit_me())
  dealer_hand.append(hit_me())
  dealer_hand.append(hit_me())

  show_hands(player_hand, dealer_hand, 0) # show player's hand and one of the dealer's cards

  passing = False
  # player turn
  while passing == False: 
    player_choice = input("Would you like to 'hit' (deal you another card) or 'pass' (end your turn)? ")

    if player_choice.lower() == 'hit':
      player_hand.append(hit_me())
      show_hands(player_hand, dealer_hand, 0)
    
    if get_score(player_hand) > 21:
      player_bust = True
      passing = True

    elif player_choice.lower() == 'pass':
      passing = True

  # end player's turn


  # handle dealer's turn
  while get_score(dealer_hand) < 17:
    dealer_hand.append(hit_me())

  # debug test
  # print(f"player score: {get_score(player_hand)}, dealer score: {get_score(dealer_hand)}")  

  if get_score(player_hand) > get_score(dealer_hand) and player_bust == False:
    player_wins = True
  elif get_score(dealer_hand) > 21 and player_bust == False:
    player_wins = True    
  elif get_score(player_hand) == get_score(dealer_hand) and player_bust == False:
    player_draw = True     
  else: # dealer score > player score
    player_wins = False



  # final results displayed. the flags above could probably be incorporated into this.   
  if player_bust == True:
    print(f"\n\nYou went over.  =S \n\n")
    print(busted)
    show_hands(player_hand, dealer_hand, 1) # in this section, we show all of the dealer's cards (the last parameter)
  elif player_wins == True:
    print(you_won)
    print("\n\n")
    show_hands(player_hand, dealer_hand, 1)
  elif player_wins == False:
    print(you_lost)
    show_hands(player_hand, dealer_hand, 1)
  elif player_draw == True:
    print(was_draw) 
    show_hands(player_hand, dealer_hand, 1)
  else:
    print("How did we get here????")
  # end game

  another_game = input("Would you like to play another game? 'y' or 'n' ")
  if another_game.lower() == 'y':
    continue_game = True
    clear_output()

  else:
    continue_game = False    
print("Thanks for playing!")    
