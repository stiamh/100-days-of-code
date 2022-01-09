from os import system, name
import art
def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users


print(art.logo)
all_bids = {}

def secret_auction(bid_record):
    highest_bid = 0
    leader = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            leader = bidder
    print(f"The highest bidder was: {leader}, they paid {highest_bid}!")

other_user = True
while other_user:
    user_name = input("Please enter your name: \n")
    user_bid = int(input("Please enter your bid: \n€"))
    all_bids[user_name] = user_bid
    new_user = input("Is there another bidder? Type 'yes' or 'no'.\n").lower()
    if new_user == "yes":
        clear()
    else:
        other_user = False
        secret_auction(all_bids)