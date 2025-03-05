
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!\nPassword designed which is hard to get by scammers")


number_of_letters_selected = int(input("How many letters you want(Enter in numbers only)\n"))
number_of_number_selected = int(input("How many numbers you want(Enter in numbers only)\n"))
number_of_symbol_selected = int(input("How many symbols you want(Enter in numbers only)\n"))

total = number_of_letters_selected + number_of_number_selected+number_of_symbol_selected

password1 = ""
password2 = []

for i in range(1, number_of_letters_selected+1):
  password1 += (random.choice(letters))
  password2.append(random.choice(letters))
print(password1)
print(password2)

for t in range(1,number_of_number_selected+1):
  password2.append(random.choice(numbers))
  password1 += random.choice(numbers)

print(password1)
print(password2)

for t in range(1,number_of_symbol_selected+1):
  password1 += random.choice(symbols)  
  password2.append(random.choice(symbols))

print(password1)
print(password2)


print(len(password1))
print(len(password2))
# random.shuffle(password1)
print(password1)
random.shuffle(password2)
print(password2)

password3 = ""
password4 = ""

for t in range(1,len(password1)+1):
  password3 += random.choice(password1)
  
print(password3)

for l in range(0,len(password2)):
  password4 += password2[l]

print(password4)
