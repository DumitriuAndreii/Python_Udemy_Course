# from art import logo
# print(logo)
# list_of_biders = []
#
# def add_bidder(name, bid):
#     new_bid = {}
#     new_bid['name'] = name
#     new_bid['bid'] = bid
#     list_of_biders.append(new_bid)
# game_over = 0
# max_bid = 0
# while not game_over:
#     name = input("what's your name? ")
#     bid = int(input("what's your bid? "))
#     add_bidder(name,bid)
#     more_bidders = input("are there any other bidders? 'yes' / 'no' ?")
#     if more_bidders == 'no':
#         game_over = 1
# print(list_of_biders)
# for _ in list_of_biders:
#     if list_of_biders[name] > max_bid:
#         max_bid = list_of_biders[name]
# print(f"the winner of the bid is {list_of_biders[name]}")

from art import logo
print(logo)
bids = {}
bidding_finished = 0

def find_highest_bidder(bidding_reord):
    highest_bid = 0
    for bidder in bidding_reord:
        bid_amount = bidding_reord[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, they won with the amount of {highest_bid}")

while not bidding_finished:
    name = input("what's your name? ")
    price = int(input("what's your bid? "))
    bids[name] = price
    should_continue = input("are there any other bidders? 'yes' / 'no' ?")
    if should_continue == "no":
        bidding_finished = 1
        find_highest_bidder(bids)
#    elif should_continue == 0:
        #clear()