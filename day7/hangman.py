import random
import hangman_art
import hangman_wordlist
import os

clear = lambda: os.system('cls')
chosen_word = random.choice(hangman_wordlist.word_list)

print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append("_")
    # display += " "
print (display)
print(hangman_art.stages[lives])
game_over = 0
while not game_over:

    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print("You have already chose this letter! Choose another one!")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word.You lose a life ")
        lives -=1
    print(hangman_art.stages[lives])
    if "_" not in display:
        game_over = 1
        print("You Have won!")
    if lives == 0:
        game_over =1
        print("you lost")
        print(chosen_word)
    print(display)