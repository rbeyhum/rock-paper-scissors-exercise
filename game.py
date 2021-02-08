# game.py

import os
import random
#from random import choice

from dotenv import load_dotenv
print("Rock, Paper, Scissors, Shoot!")

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("-------------------")
print(f"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game...")
print("-------------------")


#Asking for user input



#printing many things separated by a comma
#print("You chose: ", x)

#string concatenation
#print("You chose: " + x)

#string interpolation / format string use 

user_choice = input("Please choose either 'rock', 'paper', 'scisscors': ")

user_choice = user_choice.lower()

print(f"You chose: {user_choice}")

options = ["rock", "paper", "scissors"]

#validate the user selection
#stop the program and not try to determine the winner if the user choice is invalid



if user_choice not in options:
    print("OOPS, please choose a valid option and try again!")
    exit()

#simulating computer options and printing it
computer_choice = random.choice(options)
#computer_choice = choice(options)

print(f"The computer chose: {computer_choice}")





#determing who won - code used from Slack from William Perrone

if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh! The computer won, that's ok!")    


print("-------------------")
print("Thanks for playing. Please play again!")