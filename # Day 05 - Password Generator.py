# Day 05 - Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_password_length = nr_letters + nr_symbols + nr_numbers
p_let = []
p_num = []
p_sym = []
passw0rd = []

# get all the letters at once
for i_let in range(1, nr_letters+1):
    p_let.append(letters[random.randint(0,51)])

# get all the numbers at once
for i_num in range(1, nr_numbers+1):
    p_num.append(numbers[random.randint(0,9)])

# get all the symbols at once
for i_sym in range(1, nr_symbols+1):
    p_sym.append(symbols[random.randint(0,8)])  

passw0rd = p_let + p_num + p_sym # append the 3 lists into a single list
random.shuffle(passw0rd) # randomly sort the list
passw0rd = ''.join(passw0rd) # join them together into a string

print(f"This is your generated password: {passw0rd}")