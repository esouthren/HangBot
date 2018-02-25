# Hangman Game
import random
from draw_hangman import *
import serial
ser = serial.Serial('COM3', 9600, timeout=0)



words = ["elephant", "octopus", "rabbit", "giraffe"]

play_word = random.choice(words)

#print("Word we are playing with is... {}".format(play_word))
num_of_letters = len(play_word)


lives = 8
chosen_letters = []


def check_if_user_has_won(hidden_word, chosen_letters):
    win = True
    output_string = ""
    for c in hidden_word:
        if c in chosen_letters:
            output_string += " {} ".format(c)
        else:
            output_string += " _ "
            win = False
    print(output_string)
    if win:
        return True
    else:
        return False

# Ask the user for a letter until it gets a valid, single letter input
win = False
while True:
    valid_letter = False
    while valid_letter is False:
        if len(chosen_letters) > 0:
            print("Used letters: {}".format(sorted(chosen_letters)))

        letter = input("Please enter a letter").lower()
        if not letter.isalpha():
            print("that's not a letter!")
        elif len(letter) != 1:
            print("Just one letter!")
        elif letter in chosen_letters:
                print("You've picked that letter already!")
        else:
            valid_letter = True
            if letter not in chosen_letters:
                if letter not in play_word:
                    print("That letter is not in the word...")
                    lives -= 1

                else:
                    print("It's a match!")
                chosen_letters.append(letter)
                print_hangman(lives)
                ser.write(lives)

    if check_if_user_has_won(play_word, chosen_letters):
        print("\n\nWINNER!!!")
        break
    if lives == 0:
        print("\n\nYou're out of lives...")
        break

print("\nThanks for playing!")
