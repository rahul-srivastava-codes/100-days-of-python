# Strings are stored in array if you want any specific char use index
print("Hello"[1])  #prints e as numbering starts from 0 in coding
print("Hello"[-1]) #prints 0 as counting starts from right when negative index is given

# Tip calculator when i reached a restaurent
print("welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage of tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
total_bill = round((bill+tip*bill/100)/(number_of_people),2)
print(f"Each person should pay: ${total_bill}.")
