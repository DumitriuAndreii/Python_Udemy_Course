import random
import os
import art
import game_data

clear = lambda: os.system('cls')

# Display art

# Format data to look nice
def format_data(dict_account):
    key_values = []
    key_values = list(dict_account.values())
    print(f"Compare A: {key_values[0]},a {key_values[2]} from {key_values[3]}")
    return key_values[1]


def followers_check(acc1,acc2,guess):
    if acc1 >= acc2 and guess == 'A':
        return True
    elif acc2 >= acc1 and guess == 'B':
        return  True
    else:
        return False

# Generate a random account from the data list
random_acc1 = random.choice(game_data.data)

lives = 1
score = 0
while lives:
    print(art.logo)
    random_acc2 = random.choice(game_data.data)
    A = format_data(random_acc1)
    print(A)
    print(art.vs)
    B = format_data(random_acc2)
    print(B)
    # Ask user for a guess
    user_guess = input("Who has more followers? A or B? ")
    if followers_check(A,B,user_guess) == False:
        lives = 0
        print("You lost!")
        print(f"your score is {score}")
    else:
        random_acc1 = random_acc2
        random_acc3 = random.choice(game_data.data)
        B = random_acc3
        score += 1
        clear()

# from game_data import data
# import random
# from art import logo, vs
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()