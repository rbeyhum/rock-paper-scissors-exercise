# Rock Paper Scissors Exercise

This is the README.md file. It will explain both the steps taken to write code and setting up an environment. 

## Repository Setup

Firstly, I created a remote repository using the GitHub online interface. Then, I cloned the repository to GitHub Desktop software and chose the *Desktop* as a location to download the repo. This was done through GitHub Desktop itself and not through the command line. Moreover, using the text editor *VS Code*, I created a file called game.py which will contain all the necessary code needed to run the **Rock Paper Scissors Exercise**.
Using the command line, I navigated to the repo from there using the following command:
```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

## Environment Setup

This step entails the process of creating a virtual environment locally using the command-line. 
```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

## Customizing Player Name 

To do so, we must create two different files in our text editor. One being the .env file and the seocond being the requirements.txt file. The first file includes the content needed to customize the name such as:

        PLAYER_NAME="Rami Beyhum"
The second file allows for the installation of packages, especially the Dotenv package using the following command:
```sh
pip install -r requirements.txt
```

## The Code
### Processing and Validating User Inputs

Here, the user inputs their choice being rock, paper, or scissors. This value gets stored into a variable:
```python
user_choice
```
Then, the ``` .lower() ``` command is used in order for data validation. Here, if the user inputs rock or Rock or ROCK, the interface will understand the input in the same way. If a wrong input is put in, the command line will say that the input is invalid and the user must try again. This is done using the ``` exit() ``` keyword. 

### Simulating Computer Selection

In this exercise, the user is playing against the computer. Therefore, something must be done in the code in order to randomly select the computer's selection. Line 3 and 4 of the game.py file state:
```python
import os
import random
```
This allows the user to then call the ``` random.choice()``` in order to select a random choice for the computer's selection to play against the user. While, the os package is used for customizing the player name.

### Determining the Winner and Final Output

Using ``` if ``` statements allows to determine the winner. For example, if the user chooses rock and the computer chooses scissors, then the user wins. So, depending on the inputs, the winner is determined. 

