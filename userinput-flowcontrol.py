# Build rock paper scissor game

import sys
import random
from enum import Enum # Enum class in package enum


class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3

#print(RPS(2))    
#print(RPS.ROCK)    
#print(RPS['ROCK'])    
#print(RPS.ROCK.value)

playagain = True

while playagain:

    print('\nYour possible choices: \n 1 For Rock \n 2 For Paper \n 3 For Scissors\n\n')
    playerchoice = input('Enter your choice - ')

    playerchoiceInt = int(playerchoice)

    if playerchoiceInt < 1 or playerchoiceInt > 3:
        sys.exit('You must enter 1, 2 or 3')

    computerChoice = random.choice("123") # One of the characters will be choosen randomly
    computerChoiceInt = int(computerChoice)

    print("\nYou chose " + str(RPS(playerchoiceInt)).replace('RPS.', '') + ".")
    print("Computer chose " + str(RPS(computerChoiceInt)).replace('RPS.', '') + ".\n")

    if playerchoiceInt == 1 and computerChoiceInt == 3:
        print("🎉 You win!!")
    elif playerchoiceInt == 2 and computerChoiceInt == 1:
        print("🎉 You win!!")
    elif playerchoiceInt == 3 and computerChoiceInt == 2:
        print("🎉 You win!!")
    elif playerchoiceInt == computerChoiceInt:
        print("😍 Tie game!!")    
    else:
        print("💻 Computer wins!!")


    playagainChoice = True
    while playagainChoice: 
        playagainChoice = input("\nPlay again? Y or Yes or Q for Quit \n\n")
    
        if playagainChoice.lower() == "y":    
            playagain = True
            break
        elif playagainChoice.lower() == "q":
            print("Thanks for playing!!")
            playagain = False
            break
        else:
            print("Please enter a valid choice!!")

sys.exit("BYE!!")            