# Hangman Game
import random
from draw_hangman import *
from twilio.rest import Client
import serial
import time
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC2fa452c81d34fc2952e00022a1c6e436"
auth_token = "8e6fd396cf9a650c96a5031c43997f28"

ser = serial.Serial('COM3', 9600, timeout=0)

client = Client(account_sid, auth_token)

# A list of message objects with the properties described above
'''
for message in client.messages.list():
    if message.direction == "inbound":
        print(message.body)
        thing = message.sid
        client.messages(thing).delete()
'''
words = ["elephant", "octopus", "rabbit", "giraffe", "hackathon", "goldsmiths"]

play_word = random.choice(words)
#print("Word we are playing with is... {}".format(play_word))
num_of_letters = len(play_word)


lives = 8
chosen_letters = []

def check_twilio_messages():
    letter = "null!"
    print("Checking for messages...")
    message_id = "null"
    letters = { a:0,b:0,c:0,d:0,e:0,f:0,g:0,h:0,i:0,j:0,k:0,l:0,m:0,n:0,o:0,p:0,q:0,r:0,
    s:0,t:0,u:0,v:0,w:0,x:0,y:0,z:0}
    message_count = 0
    while message_count < 3:
        for message in client.messages.list():
            print("MESSAGE: {}".format(message.body)
            if message.direction == "inbound":
                if message.body != "":
                    choice = int(message.body)
                else:
                    choice = 0
            try:
                votes[choice] += 1
                print("New vote for {}".format(choice))
                message_count += 1
                print("message_count: {}".format(message_count))
                if message_count >= 3:
                    break
                except:
                    print("invalid vote")
            thing = message.sid
            time.sleep(2)
            client.messages(thing).delete()
    top_vote = 0
    top_vote = max(votes, key=lambda k: votes[k])
    if top_vote.lower() not in 'a b c d e f g h i j k l m n o p q r s t u v w x y z' or top_vote.lower() in chosen_letters:
        top_vote = 'z'
    return top_vote

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

        letter, message_id = check_twilio_messages()
        letter = letter.lower()

        if letter not in play_word:
            print("That letter is not in the word...")
            lives -= 1
            ##### draw_hangman(lives) function ######

        else:
            print("It's a match!")
            ###### update_drawboard() send to processing? ####
        chosen_letters.append(letter)
        print_hangman(lives)
        #ser.write(lives)

    if check_if_user_has_won(play_word, chosen_letters):
        print("\n\nWINNER!!!")
        break
    if lives == 0:
        print("\n\nYou're out of lives...")
        break

print("\nThanks for playing!")
