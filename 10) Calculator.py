num1 = input("Enter number: ")

t = "y"

while t == "y":
  result = 0
  print("+")
  print("-")
  print("*")
  print("/")
  operator = input()
  if operator == "+":
    num2 = input("Enter number again: ")
    result = int(num1) + int(num2) 
    print(f"Result: {result}")
  elif operator == "-":
    num2 = input("Enter number again: ")
    result = int(num1) - int(num2)
    print(f"Result: {result}")
  elif operator == "*":
    num2 = input("Enter number again: ")
    result = int(num1)* int(num2)
    print(f"Result: {result}")
  elif operator == "/":
    num2 = input("Enter number again: ")
    result = (int(num1)) // int(num2)
    print(f"Result: {result}")
  else:
    print(f"invalid operator")
  t = input("Do you want to perform another operation? (y/n): ")
  num1 = result
  if t == "n":
    print("See you later thanks for using me")
