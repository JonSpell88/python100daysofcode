# 1 to 100, easy = 10 guesses, hard = 5 guesses
# tell how many guesses are left each time
# too high, too low

import random

logo = """
 /$$   /$$                         /$$                                
| $$$ | $$                        | $$                                
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       
| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$      
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/      
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$            
| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$            
|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/            
                                                                      
                                                                      
                                                                      
  /$$$$$$                                                             
 /$$__  $$                                                            
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$  
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$ 
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/ 
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$_____/| $$       
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$$| $$       
 \______/  \______/  \_______/|_______/|_______/  \_______/|__/       
                                                                      
"""

# initialization zone
num_turns = 0
player_wins = False
# here is the number I'm thinking of
the_answer = random.randint(1, 100)

# function to check how the guess compares to the answer
def check_answer(guess):
  if guess < the_answer:
    return "TOO LOW"
  elif guess > the_answer:
    return "TOO HIGH"
  else:
    return "JUST RIGHT"




print(logo)
print("Welcome to the Number Guesser!")
print("I'm thinking of a number between 1 and 100.")
print("Do you want to play the easy version (10 guesses) or the hard version (5 guesses)?") 
difficulty_level = input("Choose 'easy' or 'hard' ")
if difficulty_level.lower() == 'easy':
  num_turns = 10
else:
  num_turns = 5

# loop to take in guesses, compare guess to answer
while num_turns > 0:
  print(f"You have {num_turns} guesses left.")
  guess = int(input("What is your guess? "))
  if check_answer(guess) == "TOO LOW":
    print("Your guess is too low.")
  elif check_answer(guess) == "TOO HIGH":
    print("Your guess is too high.")
  elif check_answer(guess) == "JUST RIGHT":
    player_wins = True
    num_turns = 0

  num_turns -= 1 # decrease the number of turns by 1 and repeat

# after the loop
if player_wins == True:
  print(f"You got it right! The answer was {the_answer}!")
else:  
  print(f"Sorry, you ran out of guesses. The answer was {the_answer}")
