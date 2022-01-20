#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcomee to the Tip Calculator!")
print("\n")

bill = float(input("What is the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill?: "))

tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
bill_per_person = round((total_bill / people), 2)

print(f"Each person should pay ${bill_per_person}")