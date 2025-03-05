user_choice = int(input('Type 1 for scissor, Type 2 for rock and Type 3 for paper.\n'))
computer_choice  = random.randint(0,3)
print(f"Computer choose {computer_choice}")

while(computer_choice == user_choice):
  computer_choice = random.randint(1,3)

# print(f"Computer choose {computer_choice}")

if user_choice<computer_choice:
  print("Computer wins!")
elif user_choice>3:
  print("Invalid input you moron")  
else:
  print("You win!")  


# few ugs are there ca you fix it
