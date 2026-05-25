letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("Welcome to the PyPassword Generator!")
no_of_letters =int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
if no_of_letters == 0 or no_of_symbols == 0 or no_of_numbers == 0:
  print("invalid input please check the entered number should be greater than zero")
elif no_of_letters > 0 and no_of_symbols > 0 and no_of_numbers > 0:
  password =""
  for letter in range(1,no_of_letters+1):
    password+=random.choice(letters)
  for symbol in range(1,no_of_symbols+1):
    password+=random.choice(symbols)
  for number in range(1,no_of_numbers+1):
    password+=random.choice(numbers)
  password_list = list(password)
  random.shuffle(password_list) 
  strongpassword = "".join(password_list)
  
  print(f"Password Successfully generated - {strongpassword}")    