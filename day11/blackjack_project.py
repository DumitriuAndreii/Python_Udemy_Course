############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

game_over = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_hand = []
    random_hand.append(random.choice(cards))
    random_hand.append(random.choice(cards))
    return random_hand
# calculating user hand and their sum
user_hand = []
user_first_card = random.choice(cards)
user_second_card = random.choice(cards)
user_hand.append(user_first_card)
user_hand.append(user_second_card)
print(f"your hand is {user_hand}")
user_sum = user_first_card + user_second_card

# calculating computers hand and their sum
computer_hand = []
computer_first_card = random.choice(cards)
computer_second_card = random.choice(cards)
computer_hand.append(computer_first_card)
computer_hand.append(computer_second_card)
print(f"dealer's hand is {computer_hand}")
computer_sum = computer_first_card + computer_second_card

if computer_sum == 21:
    game_over = 1
    print("You lose")
elif user_sum == 21:
    game_over = 1
    print("You win")

while not game_over:
    # computer_random_card = random.choice(cards)
    if user_sum >21 and (11 in user_hand):
        user_hand = user_hand - 10
    elif user_sum >21 and (11 not in user_hand):
        game_over = 1
        print("you lose")
        break
    another_card = input("do you want another card? y or n ")
    while another_card != 'n':
        if another_card == 'y':
            user_random_card = random.choice(cards)
            user_hand.append(user_random_card)
            user_sum = user_sum + user_random_card
            print(f"your hand is {user_hand}")
            if user_sum > 21 and (11 not in user_hand):
                game_over = 1
                print("you lose")
                break
            elif user_sum >21 and (11 in user_hand):
                user_hand = user_hand - 10
                user_hand.index(11) = 1

            another_card = input("do you want another card? y or n ")















##################### Hints #####################



#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.