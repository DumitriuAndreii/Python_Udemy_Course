import random
from art import logo
import os
clear = lambda: os.system('cls')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return (sum(cards))


def compare(user_score,computer_score):
    if computer_score == 0:
        return "Computer wins "
    elif user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "you went a lil too far"
    elif computer_score > 21:
        return "oponent went over"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards are {user_cards} and your score is {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type y to get another card or n if u do not want  ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand is {user_cards}, with a final score of {user_score}")
    print(f"computer's final hand is {computer_cards}, with a final score of {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game of blackjack? ") == 'y':
    clear()
    play_game()