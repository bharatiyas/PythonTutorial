import sys
import argparse
import random


def guess_the_number(name = "Player1"):

    number_of_rounds = 0
    player_won = 0

    choice = ["1", "2", "3", "4"]

    def play():
        nonlocal number_of_rounds
        nonlocal player_won
        nonlocal name

        play_again = True

        while play_again:
            
            number_of_rounds += 1

            player_choice = input(f"{name}, please choose a number between 1 to 4: ")

            if player_choice not in choice:
                print("You chose wrong number")
                continue

            computer_choice = random.choice("1234")
            print(f"Compuer chose: {computer_choice}")
            if player_choice == computer_choice:
                print(f"{name}, you guessed it right. You won!!")
                player_won += 1
            else:
                print(f"{name}, sorry your guess was incorrect. You lost!!")                
            while True:
                cont = input(f"{name}, do you want to play again? [Y/N]: ")
                if cont.lower() == "y":
                    break
                elif cont.lower() == "n":
                    play_again = False
                    break
                else:
                    print(f"{name}, please enter Y or N")


        print(f"Final result: \n Total Rounds - {number_of_rounds} \n {name} won - {player_won}")
        print(f"{name}, you winning percentage: {player_won / number_of_rounds * 100}%")
        print(f"{name}, thanks for playing! Bye!!")

    return play

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Take planer name as input for the game")

    parser.add_argument(
        '-n',
        '--name',
        required = True,
        metavar = 'N',
        type = str,
        help = "Enter name of the player playing the game")

    args = parser.parse_args()
    play_the_game = guess_the_number(args.name)
    play_the_game()
        


