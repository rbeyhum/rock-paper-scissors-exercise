# game.py

import random
#from random import choice

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

#validate the user selection
#stop the program and not try to determine the winner if the user choice is invalid

user_choice.lower()

if user_choice not in options:
    print("OOPS, please choose a valid option!")
    exit()


computer_choice = random.choice(options)
#computer_choice = choice(options)

print(f"The computer chose: {computer_choice}")





#determing who won

if computer_choice == user_choice:
    print("It's tie!")
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

#simulating a computer input

#print("The computer chose: 'paper'")
#
##determining who won
#
#print("-------------------")
#print("Oh, the computer won. It's ok.")
#print("-------------------")
#print("Thanks for playing. Please play again!")