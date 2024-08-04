logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from IPython.display import clear_output  # for use in clearing the output, works in Google Colab

print(logo)
print("Welcome to the secret auction program!")
first_choice = input("What is the name of the first bidder? ") # take the first inputs on name and amount
first_bid = float(input("What is the amount of the bid? $"))
choices = 'yes'
bidding_list = {} # set up empty dictionary to hold list of bidders and amounts
bidding_list[first_choice] = first_bid   # first bid goes into dictionary here
while choices.lower() != "no":  # loops while there are still bidders
  bid_name = '' # initialize the variables
  bid_amount = 0.00
  choices = input("Are there any other bidders? yes/no ")
  if choices.lower() == "yes":
    clear_output() # clears the output
    bid_name = input("What is the name of the next bidder?")
    bid_amount = float(input("What is the amount of the bid?"))
    bidding_list[bid_name] = bid_amount
  else:
    choices = "no"

# note: there could be a more efficient way to do this, but this is where we are in the class
max_bid = 0
max_bidder = ''
for key in bidding_list:
  if bidding_list[key] > max_bid:
    max_bid = bidding_list[key]
    max_bidder = key


# print(bidding_list) debug
print(f"The winner of this auction is {max_bidder} with a bid of ${max_bid : .2f}!")