print("Welcome to Treasure Island\nYour  mission is to find the treasure")
direction = input("Left or Right\n")
if direction == "left":
  print(direction)
  x1=input("Swim or Wait\n")  
  if x1 == "swim":
    input("Swim or anything else\n")
    print("Attacked by trout \n Game over.\n")
  else: 
    wait=input("Type wait\n")
    if wait == "wait":
      door = input("Which door\n")
      if door == "blue":
        print("Eaten by beasts\nGame over.\n")
      elif door == "red":
        print("Burned by fire\nGame over.\n")
      elif door == "yellow":
        print("You win buddy\n")
      else:
        print("Game over\n")      
else:
  input("Right or anything else\n")
  print("Fall into a hole. \n Game Over")
