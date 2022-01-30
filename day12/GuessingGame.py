import random
from art import logo
print(logo)

print("Welcome to the guessing game")
print("I'm thinking at a number between 1 and 100 ")
#choosing the number we are gonna play with
random_number = random.choice(range(1,101))
print(f"pssst the corect answer is {random_number}")


difficulty = input("Choose a difficulty. Easy or Hard ")
if difficulty == 'easy':
    print("you chose the easy way! You got 10 lives")
    lives = 10
else:
    print("you chose the hard way! You got 5 lives")
    lives = 5

def compare(guess, chosen_number):
    global lives
    if guess > chosen_number:
        lives -=1
        return "Too high! Try smth lower"
    elif guess < chosen_number:
        lives -= 1
        return "Too low!"
    else:
        lives = 0
        return "You got it well done! "

while lives:
    player_guess = int(input("Take a guess "))
    print(compare(player_guess,random_number))
    if lives != 0:
        print(f"tou got {lives} attempts remaining to guess the number")
    else:
        print("GAME OVER")