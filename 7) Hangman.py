import random as rd
words = ["Rahul" , "boke", "handsome", "location", "Ram" ]
chosen_word = rd.choice(words).lower()
print(chosen_word)

game_over = False
placeholder = ""
  
length = len(chosen_word)
lives = 6

for i in range(length):
  placeholder += "_"
print(placeholder)

correct_loop = []

while not game_over:
  guess = input("Guess a letter\n").lower();    

  display = ""
  for i in chosen_word:
    if i == guess:
      display += i
      correct_loop.append(i) 
    elif i in correct_loop:
      display+= i;      
    else:
      display += "_"
  print(display)

  if guess not in chosen_word:
    lives -= 1
    print(f"You have {lives} lives left.")
    if lives == 0:
      game_over = True
      print("Game over! You lost.")
      break

  if "_" not in display:
    game_over = True
    print("You win!")
    
  
  

