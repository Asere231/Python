from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the best silent betting venue!!!")

isGame = True
bids = {}

def highest_bidder(bids):
    max = 0
    name = ""
    for key in bids:
        if bids[key] > max:
            max = bids[key]
            name = key
    print(f"The winner is {name} with a bid of ${max}.")


while isGame:
    name = input("What is your name? ")
    price = int(input("How much will you bet? $"))
    bids[name] = price
    more = input('Are there any other bidders? "yes" or "no" ')

    if more == "no":
        isGame = False
        clear()
    elif more == "yes":
        clear()

highest_bidder(bids)



    
     


