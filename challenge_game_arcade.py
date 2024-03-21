import argparse
import challenge_guess_number
import cli_rps



def arcade_games(name):
    
    def play():

        nonlocal name

        player_choice = input(
            f"\n{name}, please enter... \n1 for Rock, Paper, Scissors\n2 for Number Guess :\n\n")

        if player_choice not in ["1", "2"]:
            print(f"{name}, please enter 1 or 2")
            return play_rps()

        player_choice_int = int(player_choice)

        play_again = True

        while play_again:

            if player_choice_int == 1:
                play_rps = cli_rps.rps(name)
                play_rps()
            else:
                play_guess_num = challenge_guess_number.guess_the_number(name) 
                play_guess_num()

            while True:
                cont = input(f"{name}, do you want to play again? [Y/N]: ")
                if cont.lower() == "y":
                    break
                elif cont.lower() == "n":
                    play_again = False
                    break
                else:
                    print(f"{name}, please enter Y or N")

    return play   

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(   
        "-n",              
        "--name",          
        metavar="name",     
        required=True, 
        help="Name of the person playing the game"
    )

    args = parser.parse_args()

    play_arcade = arcade_games(args.name)
    play_arcade()


    