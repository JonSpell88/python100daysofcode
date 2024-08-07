# Day 10 - simple calculator, using a dictionary to cache the operations

# So, we meet again, Cal-cu-lat-OR!

from IPython.display import clear_output

logo = f"""
     _____________________
    |  _________________  |
    | |                 | |
    | |  07734          | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """

# bank of functions
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    print("Error. Cannot divide by zero!")
    return
  else:
    return num1 / num2

def to_the_power(num1, num2):
  return num1 ** num2

def modulus(num1, num2):
  return num1 % num2

# this adds functionality to special keys
operandus = {"+": add, "-": subtract, "*": multiply, "/": divide, "POW": to_the_power, "%": modulus}

# operandus["*"](4,8) # so crazy!

print(logo)
print("Welcome to the Python Calculator!")
first_num = float(input("What is the first number? "))

program_exit = False

while program_exit == False:


  for key in operandus:
    print(key)
  
  operation = input("Pick an operation above, or type 'exit' to leave.")
  if operation == "exit":
    program_exit = True
    break
  else:
    next_num = float(input("What's the next number? "))
    result = operandus[operation](first_num, next_num)
    print(f"{first_num} {operation} {next_num} = {result}")

  print(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.")
  if input() == "y":
    first_num = result
  else:
    clear_output()
    first_num = float(input("What is the first number? "))