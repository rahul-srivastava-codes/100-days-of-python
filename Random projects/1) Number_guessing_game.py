import random
print("Welcome babes to Number guessing game!")
a = int(input("Enter your favorite smallest number:\n"))
b = int(input("Enter your favorite largest number:\n"))

random_number = random.randint(a,b)
# print(random_number)
lives = 5

while lives>0:
  guess = int(input("Enter number you guesses:"))
  if guess == random_number:
    print("Congratulation boy you won")
    break
  else: 
    if lives != 1:      
      print(f"Try one more time you have {lives} lives left")
      lives -= 1
      if guess < random_number:
        print("Try larger number than this")
      else:
        print("Try smaller number than this")  
    else:
      print("bad luck")   

if lives == 0:
  print(f"Sorry, you lost. The correct number was {random_number}")
  print("Play one more time")    
     
  
