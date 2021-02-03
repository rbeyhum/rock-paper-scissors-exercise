# game.py

import random


print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking for user input
#


#printing many things separated by a comma
#print("You chose: ", x)

#string concatenation
#print("You chose: " + x)

#string interpolation / format string use 

user_choice = input("Please choose either 'rock', 'paper', 'scisscors': ")



print(f"You chose: {user_choice}")



options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


print(f"The computer chose: {computer_choice}")


#simulating a computer input

#print("The computer chose: 'paper'")
#
##determining who won
#
#print("-------------------")
#print("Oh, the computer won. It's ok.")
#print("-------------------")
#print("Thanks for playing. Please play again!")