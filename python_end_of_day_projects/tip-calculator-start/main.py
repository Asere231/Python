#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = float(input("What was the total check? $"))
percent = int(input("How much will you tip? 10%, 12%, or 15% ? "))
people = int(input("How many people to split the bill? "))


bill_with_tip = percent / 100 * total + total

total_per_person = bill_with_tip / people

# This will help us format the output, because even tho the round fuction is working, it cannot display an extra cero, like so, 33.6. This formatting will do that for us; 33.60
bill = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${bill}")
