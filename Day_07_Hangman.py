# Day 07 - Hangman
import random

# set up word list and letters list
master_word_list = [
'aircraft',	'artist',	'backbone',	'baseball',	'bathroom',	'battery',	'beach',	'beaver',	'beehive',	'bicycle',	'birthday',	'blading',	'blowfish',	'bomb',	'boot',	'bowtie',	'brain',	'bulb',	'cake',	'cake',	'camera',	'cello',	'chalk',	'chin',	'circus',	'clam',	'coal',	'computer',	'cowboy',	'deep',	'doghouse',	'dollar',	'dominoes',	'door',	'doormat',	'dryer',	'electricity',	'face',	'flagpole',	'flute',	'fries',	'frog',	'garbage',	'garden',	'gate',	'gingerbread',	'hair',	'half',	'happy',	'hockey',	'hook',	'horse',	'knee',	'lawnmower',	'light',	'lighthouse',	'lightsaber',	'mailman',	'mattress',	'money',	'mushroom',	'nature',	'newspaper',	'outside',	'pajamas',	'palace',	'park',	'password',	'peach',	'pelican',	'pepper',	'photograph',	'pineapple',	'pinwheel',	'pirate',	'platypus',	'popsicle',	'pretzel',	'purse',	'queen',	'quilt',	'rain',	'rainbow',	'roller',	'round',	'sailboat',	'salt',	'scale',	'school',	'shallow',	'skate',	'skirt',	'snowball',	'soda',	'song',	'spare',	'spool',	'spring',	'sprinkler',	'state',	'stingray',	'stomach',	'suitcase',	'swing',	'teapot',	'thief',	'ticket',	'toast',	'treasure',	'trip',	'tusk',	'watering',		'whisk',	'whistle'    
]

letters = [
'a',	'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z',
]

hangman_image = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''' , '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

# 126 words
print("Welcome to Jon's Hangman!\n\n")
# choose word randomly
secret_word = random.choice(master_word_list)
# secret_word = master_word_list[random.randint(1, 126)-1]
secret_word_as_list = list(secret_word) # used for guessing
public_word_as_list = [] # to show the word as blanks
missed_guess_count = 0

for i in secret_word_as_list:
  public_word_as_list.append("_ ") # creates a public "word" to show the user with spaces in between for readability

# print(secret_word)
print(''.join(public_word_as_list)) # this prints a sequence of blanks that represent the secret word (same number of blanks as letters)

print("\n\n") # nice to have a couple of lines after the blanked secret word


print("Letters to pick from : [", ''.join(letters), "]") # displays a list of letters that haven't been chosen yet

while missed_guess_count < 6: # at a count of 6 you have a full hanged man

  print(hangman_image[missed_guess_count])

  guess = input("Guess a letter: ").lower() # accepts input and makes it lowercase
  # print(guess)

  for j in range(0, len(secret_word_as_list)): # loop through the word, changing public word to show correctly guessed letters
    if secret_word_as_list[j] == guess:
      public_word_as_list[j] = guess
      
  for k in range(len(letters)): # loop through alphabet letters and replace them with an underscore if guessed
    if letters[k] == guess:
      letters[k] = '_'

  if guess not in secret_word_as_list: # if the letter wasn't in the secret word, this advances the misses count and will reflect in the next drawn hangman
    missed_guess_count += 1  
    

  print(''.join(public_word_as_list))
  if ''.join(public_word_as_list) == secret_word: # if all of the public word blanks have been filled in, you win
    print(f"You won! The word was {secret_word}!")
    break

  print("Letters to pick from : [", ''.join(letters), "]") # show the letters that are still usable

             
# this happens after the while loop exits
if missed_guess_count >= 6:
  print(f"You lost! The word was {secret_word}")