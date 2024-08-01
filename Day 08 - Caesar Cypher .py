# Day 08 - Caesar Cypher 

def go_encrypt(message, shift_count):
  encrypted_message = ''
  for i in range(0, len(message)):  # for each character in message
    if ord(message[i]) >= 97 and ord(message[i]) <= 122: # first, check to see if it's a lowercase letter

      if ord(message[i]) + shift_count > 122: # then, check to see if the letter plus the shift amount would put it past z
        encrypted_message += chr(ord(message[i]) + shift_count - 26)  # letters[ord(message[i]) + shift_count - 26]  # if so, subtract 26 so that it loops back around to a
      else:
        encrypted_message += chr(ord(message[i]) + shift_count) #letters[ord(message[i]) + shift_count] # if not, just add the letter that's the shifted one

    elif ord(message[i]) >= 65 and ord(message[i]) <= 90:
      if ord(message[i]) + shift_count > 90:
        encrypted_message += chr(ord(message[i]) + shift_count - 26)  # -26?
      else:
        encrypted_message +=  chr(ord(message[i]) + shift_count)

    else:
      encrypted_message += message[i] # handles spaces and other non-alpha characters
#    print(encrypted_message)

  print(f"This is your encrypted message: {encrypted_message}")

def go_decrypt(message, shift_count):
  unencrypted_message = ''
  shift_count = (-1) * shift_count

  for i in range(0, len(message)):  # for each character in message
    if ord(message[i]) >= 97 and ord(message[i]) <= 122: # first, check to see if it's a lowercase letter

      if ord(message[i]) + shift_count < 97: # then, check to see if the letter minus the shift amount would put it before a
        unencrypted_message += chr(ord(message[i]) + shift_count + 26)  # if so, add 26 so that it loops back around to z
      else:
        unencrypted_message += chr(ord(message[i]) + shift_count) # if not, just add the letter that's the shifted one

    elif ord(message[i]) >= 65 and ord(message[i]) <= 90:
      if ord(message[i]) + shift_count < 65:
        unencrypted_message += chr(ord(message[i]) + shift_count + 26)  # -26?
      else:
        unencrypted_message +=  chr(ord(message[i]) + shift_count)

    else:
      unencrypted_message += message[i] # handles spaces and other non-alpha characters
#    print(encrypted_message)

  print(f"This is your unencrypted message: {unencrypted_message}")


#print(logo)
print("Welcome to the Caesar Cypher! You will choose to encode or decode, with a message and a number to shift.")
choice = input("Type 'encode' to encrypt, 'decode' to decrypt, 'exit' to exit the program ")
while choice.lower() != "exit":
  msg = input("Type your message: ")
  shiftiness = int(input("Enter the shift number: "))

  if choice == 'encode':
    go_encrypt(msg, shiftiness)
  elif choice == 'decode':
    go_decrypt(msg, shiftiness)
  elif choice == 'exit':
    break

  choice = input("Type 'encode' to encrypt, 'decode' to decrypt, 'exit' to exit the program ").lower()