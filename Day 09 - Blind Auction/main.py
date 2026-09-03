from art import logo
print(logo)
# TODO-1: Ask the user for input
yes_or_no = "yes"
bids = {}

def bid_winner(bidding_list):
    highest_bid = 0
    for bidder in bidding_list:
        if bidding_list[bidder] > highest_bid:
            highest_bid = bidding_list[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while yes_or_no != "no":

    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name]=price


    # TODO-3: Whether if new bids need to be added
    yes_or_no = input('Are there any other bidders? Type "yes" or "no". ').lower()
    if yes_or_no == "no":
        bid_winner(bids)
        break
    elif yes_or_no == "yes":
        print("\n"*100)
        continue
    # TODO-4: Compare bids in dictionary
