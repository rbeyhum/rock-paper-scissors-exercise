# game.py

print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking for user input

x = input("Please choose either 'rock', 'paper', 'scisscors': ")


#printing many things separated by a comma
print("You chose: ", x)

#string concatenation
print("You chose: " + x)

#string interpolation / format string use 
print(f"You chose: ", {x})


exit()



#simulating a computer input

print("The computer chose: 'paper'")

#determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")