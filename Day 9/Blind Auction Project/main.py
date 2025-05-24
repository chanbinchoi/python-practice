# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# from art import logo
#
# Auction_dictionary = {}
# bidding = ""
#
# print(logo)
# while bidding == "" or bidding.lower() == "yes":
#     if bidding.lower() == "yes":
#         print("\n" * 100)
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     Auction_dictionary[name] = price
#     bidding = input("Are there any other bidders? Type 'yes or 'no'.")
#
# winner_price = 0
# winner_name = ""
# for bid in Auction_dictionary:
#     if winner_price < Auction_dictionary[bid]:
#         winner_price = Auction_dictionary[bid]
#         winner_name = bid
#
# print(f"The winner is {winner_name} with a bid of ${winner_price}")

from art import logo
import os

print(logo)

Auction_dictionary = {}
bidding = "yes"

while bidding.lower() == "yes":
    name = input("What is your name?: ")

    while True:
        try:
            price = int(input("What is your bid?: $"))
            break
        except ValueError:
            print("Please enter a valid number.")

    Auction_dictionary[name] = price
    bidding = input("Are there any other bidders? Type 'yes' or 'no': ")

    if bidding.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

winner_name = max(Auction_dictionary, key=Auction_dictionary.get)
winner_price = Auction_dictionary[winner_name]

print(f"The winner is {winner_name} with a bid of ${winner_price}")
