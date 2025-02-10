print("Welcome to the tip calculator.")
bill=float(input("What was the total bill?"))
tipAmount=float(input("How much would you like to give? 10,12 or 15?"))
peopleAmount=int(input("How many people to split the bill?"))
billForPerson=(bill*(tipAmount/100+1))/peopleAmount
print(f"Each person should pay ${round(billForPerson,2)}")
