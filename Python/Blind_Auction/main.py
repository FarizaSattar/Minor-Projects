# Function to clear the console screen
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to find and print the highest bidder
def calculate_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

def blind_auction():
    bids = {}
    bidding_finished = False
    
    while not bidding_finished:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        
        bids[name] = bid
        
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        
        if should_continue == "no":
            bidding_finished = True
            calculate_highest_bidder(bids)
        elif should_continue == "yes":
            clear_screen()
        else:
            print("Please type 'yes' or 'no'.")

# Start the auction
blind_auction()
